"""
Database module for Clinic Management System
Handles all database operations using SQLite
"""

import sqlite3
import os
from datetime import datetime
import hashlib


class DatabaseManager:
    """Manages database connections and operations"""
    
    def __init__(self, db_name="database/clinic.db"):
        """Initialize database manager and create tables if they don't exist"""
        self.db_path = db_name
        
        # Create database directory if it doesn't exist
        os.makedirs(os.path.dirname(db_name), exist_ok=True)
        
        self._create_tables()
    
    def get_connection(self):
        """Get database connection"""
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row
            return conn
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            return None
    
    def _create_tables(self):
        """Create all required tables"""
        conn = self.get_connection()
        if not conn:
            return
        
        cursor = conn.cursor()
        
        try:
            # Users table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    full_name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    phone TEXT,
                    role TEXT DEFAULT 'user',
                    is_verified INTEGER DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Email verification codes table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS verification_codes (
                    code_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL,
                    verification_code TEXT NOT NULL UNIQUE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    expires_at TIMESTAMP,
                    is_used INTEGER DEFAULT 0,
                    FOREIGN KEY (username) REFERENCES users(username)
                )
            ''')
            
            # Patients table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS patients (
                    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    full_name TEXT NOT NULL,
                    age INTEGER,
                    gender TEXT,
                    phone TEXT,
                    address TEXT,
                    email TEXT,
                    blood_group TEXT,
                    medical_history TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Doctors table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS doctors (
                    doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    specialization TEXT,
                    phone TEXT,
                    email TEXT,
                    qualification TEXT,
                    experience_years INTEGER,
                    available_days TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Appointments table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS appointments (
                    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    patient_id INTEGER NOT NULL,
                    doctor_id INTEGER NOT NULL,
                    appointment_date TEXT NOT NULL,
                    appointment_time TEXT NOT NULL,
                    status TEXT DEFAULT 'scheduled',
                    notes TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
                    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
                )
            ''')
            
            # Medicines table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS medicines (
                    medicine_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    medicine_name TEXT NOT NULL,
                    quantity INTEGER,
                    price REAL,
                    expiry_date TEXT,
                    manufacturer TEXT,
                    description TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Billing table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS billing (
                    bill_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    patient_id INTEGER NOT NULL,
                    amount REAL,
                    payment_method TEXT,
                    status TEXT DEFAULT 'pending',
                    bill_date TEXT,
                    notes TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
                )
            ''')
            
            conn.commit()
            print("Database tables created successfully")
            
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")
        finally:
            conn.close()
    
    # User operations
    def register_user(self, username, password, full_name, email, phone=""):
        """Register a new user"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            # Hash password
            hashed_password = self._hash_password(password)
            
            cursor.execute('''
                INSERT INTO users (username, password, full_name, email, phone)
                VALUES (?, ?, ?, ?, ?)
            ''', (username, hashed_password, full_name, email, phone))
            
            conn.commit()
            conn.close()
            return True, "User registered successfully"
        except sqlite3.IntegrityError:
            return False, "Username or email already exists"
        except Exception as e:
            return False, f"Registration error: {str(e)}"
    
    def login_user(self, username, password):
        """Authenticate user"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
            user = cursor.fetchone()
            conn.close()
            
            if user and self._verify_password(password, user['password']):
                return True, user
            else:
                return False, None
        except Exception as e:
            return False, f"Login error: {str(e)}"
    
    def _hash_password(self, password):
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def _verify_password(self, password, hashed_password):
        """Verify password"""
        return self._hash_password(password) == hashed_password
    
    # Email verification operations
    def create_verification_code(self, username, email, verification_code, expires_at=None):
        """Create a verification code for email verification"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO verification_codes (username, email, verification_code, expires_at)
                VALUES (?, ?, ?, ?)
            ''', (username, email, verification_code, expires_at))
            
            conn.commit()
            conn.close()
            return True, "Verification code created"
        except Exception as e:
            return False, f"Error creating verification code: {str(e)}"
    
    def verify_email(self, username, verification_code):
        """Verify email with code and mark user as verified"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            # Check if verification code exists and is valid
            cursor.execute('''
                SELECT * FROM verification_codes 
                WHERE username = ? AND verification_code = ? AND is_used = 0
            ''', (username, verification_code))
            
            code_record = cursor.fetchone()
            
            if not code_record:
                conn.close()
                return False, "Invalid or expired verification code"
            
            # Mark verification code as used
            cursor.execute('''
                UPDATE verification_codes 
                SET is_used = 1 
                WHERE code_id = ?
            ''', (code_record['code_id'],))
            
            # Mark user as verified
            cursor.execute('''
                UPDATE users 
                SET is_verified = 1 
                WHERE username = ?
            ''', (username,))
            
            conn.commit()
            conn.close()
            return True, "Email verified successfully"
        except Exception as e:
            return False, f"Error verifying email: {str(e)}"
    
    def is_user_verified(self, username):
        """Check if user is verified"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('SELECT is_verified FROM users WHERE username = ?', (username,))
            result = cursor.fetchone()
            conn.close()
            
            return result['is_verified'] == 1 if result else False
        except Exception as e:
            print(f"Error checking verification status: {str(e)}")
            return False
    
    def get_verification_code(self, username):
        """Get latest verification code for a user"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT * FROM verification_codes 
                WHERE username = ? AND is_used = 0
                ORDER BY created_at DESC LIMIT 1
            ''', (username,))
            
            result = cursor.fetchone()
            conn.close()
            
            return dict(result) if result else None
        except Exception as e:
            print(f"Error fetching verification code: {str(e)}")
            return None
    
    # Patient operations
    def add_patient(self, full_name, age, gender, phone, address, email="", blood_group="", medical_history=""):
        """Add new patient"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO patients (full_name, age, gender, phone, address, email, blood_group, medical_history)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (full_name, age, gender, phone, address, email, blood_group, medical_history))
            
            conn.commit()
            conn.close()
            return True, "Patient added successfully"
        except Exception as e:
            return False, f"Error adding patient: {str(e)}"
    
    def get_all_patients(self):
        """Get all patients"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM patients ORDER BY created_at DESC')
            patients = cursor.fetchall()
            conn.close()
            
            return [dict(patient) for patient in patients]
        except Exception as e:
            print(f"Error fetching patients: {str(e)}")
            return []
    
    def get_patient(self, patient_id):
        """Get specific patient"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM patients WHERE patient_id = ?', (patient_id,))
            patient = cursor.fetchone()
            conn.close()
            
            return dict(patient) if patient else None
        except Exception as e:
            print(f"Error fetching patient: {str(e)}")
            return None
    
    def update_patient(self, patient_id, full_name, age, gender, phone, address, email="", blood_group="", medical_history=""):
        """Update patient information"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                UPDATE patients 
                SET full_name = ?, age = ?, gender = ?, phone = ?, address = ?, 
                    email = ?, blood_group = ?, medical_history = ?, updated_at = CURRENT_TIMESTAMP
                WHERE patient_id = ?
            ''', (full_name, age, gender, phone, address, email, blood_group, medical_history, patient_id))
            
            conn.commit()
            conn.close()
            return True, "Patient updated successfully"
        except Exception as e:
            return False, f"Error updating patient: {str(e)}"
    
    def delete_patient(self, patient_id):
        """Delete patient"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('DELETE FROM patients WHERE patient_id = ?', (patient_id,))
            
            conn.commit()
            conn.close()
            return True, "Patient deleted successfully"
        except Exception as e:
            return False, f"Error deleting patient: {str(e)}"
    
    def search_patients(self, search_term):
        """Search patients by name or phone"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT * FROM patients 
                WHERE full_name LIKE ? OR phone LIKE ? OR patient_id LIKE ?
                ORDER BY full_name
            ''', (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))
            
            patients = cursor.fetchall()
            conn.close()
            
            return [dict(patient) for patient in patients]
        except Exception as e:
            print(f"Error searching patients: {str(e)}")
            return []
    
    # Doctor operations
    def add_doctor(self, name, specialization, phone, email, qualification="", experience_years=0, available_days=""):
        """Add new doctor"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO doctors (name, specialization, phone, email, qualification, experience_years, available_days)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (name, specialization, phone, email, qualification, experience_years, available_days))
            
            conn.commit()
            conn.close()
            return True, "Doctor added successfully"
        except Exception as e:
            return False, f"Error adding doctor: {str(e)}"
    
    def get_all_doctors(self):
        """Get all doctors"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM doctors ORDER BY name')
            doctors = cursor.fetchall()
            conn.close()
            
            return [dict(doctor) for doctor in doctors]
        except Exception as e:
            print(f"Error fetching doctors: {str(e)}")
            return []
    
    def get_doctor(self, doctor_id):
        """Get specific doctor"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM doctors WHERE doctor_id = ?', (doctor_id,))
            doctor = cursor.fetchone()
            conn.close()
            
            return dict(doctor) if doctor else None
        except Exception as e:
            print(f"Error fetching doctor: {str(e)}")
            return None
    
    def update_doctor(self, doctor_id, name, specialization, phone, email, qualification="", experience_years=0, available_days=""):
        """Update doctor information"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                UPDATE doctors 
                SET name = ?, specialization = ?, phone = ?, email = ?, 
                    qualification = ?, experience_years = ?, available_days = ?, updated_at = CURRENT_TIMESTAMP
                WHERE doctor_id = ?
            ''', (name, specialization, phone, email, qualification, experience_years, available_days, doctor_id))
            
            conn.commit()
            conn.close()
            return True, "Doctor updated successfully"
        except Exception as e:
            return False, f"Error updating doctor: {str(e)}"
    
    def delete_doctor(self, doctor_id):
        """Delete doctor"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('DELETE FROM doctors WHERE doctor_id = ?', (doctor_id,))
            
            conn.commit()
            conn.close()
            return True, "Doctor deleted successfully"
        except Exception as e:
            return False, f"Error deleting doctor: {str(e)}"
    
    def search_doctors(self, search_term):
        """Search doctors by name or specialization"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT * FROM doctors 
                WHERE name LIKE ? OR specialization LIKE ?
                ORDER BY name
            ''', (f"%{search_term}%", f"%{search_term}%"))
            
            doctors = cursor.fetchall()
            conn.close()
            
            return [dict(doctor) for doctor in doctors]
        except Exception as e:
            print(f"Error searching doctors: {str(e)}")
            return []
    
    # Appointment operations
    def add_appointment(self, patient_id, doctor_id, appointment_date, appointment_time, status="scheduled", notes=""):
        """Add new appointment"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO appointments (patient_id, doctor_id, appointment_date, appointment_time, status, notes)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (patient_id, doctor_id, appointment_date, appointment_time, status, notes))
            
            conn.commit()
            conn.close()
            return True, "Appointment booked successfully"
        except Exception as e:
            return False, f"Error booking appointment: {str(e)}"
    
    def get_all_appointments(self):
        """Get all appointments"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM appointments ORDER BY appointment_date DESC, appointment_time DESC')
            appointments = cursor.fetchall()
            conn.close()
            
            return [dict(appt) for appt in appointments]
        except Exception as e:
            print(f"Error fetching appointments: {str(e)}")
            return []
    
    def get_appointment(self, appointment_id):
        """Get specific appointment"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM appointments WHERE appointment_id = ?', (appointment_id,))
            appointment = cursor.fetchone()
            conn.close()
            
            return dict(appointment) if appointment else None
        except Exception as e:
            print(f"Error fetching appointment: {str(e)}")
            return None
    
    def update_appointment(self, appointment_id, patient_id, doctor_id, appointment_date, appointment_time, status="scheduled", notes=""):
        """Update appointment"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                UPDATE appointments 
                SET patient_id = ?, doctor_id = ?, appointment_date = ?, appointment_time = ?, status = ?, notes = ?
                WHERE appointment_id = ?
            ''', (patient_id, doctor_id, appointment_date, appointment_time, status, notes, appointment_id))
            
            conn.commit()
            conn.close()
            return True, "Appointment updated successfully"
        except Exception as e:
            return False, f"Error updating appointment: {str(e)}"
    
    def delete_appointment(self, appointment_id):
        """Delete appointment"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('DELETE FROM appointments WHERE appointment_id = ?', (appointment_id,))
            
            conn.commit()
            conn.close()
            return True, "Appointment cancelled successfully"
        except Exception as e:
            return False, f"Error deleting appointment: {str(e)}"
    
    # Medicine operations
    def add_medicine(self, medicine_name, quantity, price, expiry_date, manufacturer="", description=""):
        """Add new medicine"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO medicines (medicine_name, quantity, price, expiry_date, manufacturer, description)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (medicine_name, quantity, price, expiry_date, manufacturer, description))
            
            conn.commit()
            conn.close()
            return True, "Medicine added successfully"
        except Exception as e:
            return False, f"Error adding medicine: {str(e)}"
    
    def get_all_medicines(self):
        """Get all medicines"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM medicines ORDER BY medicine_name')
            medicines = cursor.fetchall()
            conn.close()
            
            return [dict(med) for med in medicines]
        except Exception as e:
            print(f"Error fetching medicines: {str(e)}")
            return []
    
    def get_medicine(self, medicine_id):
        """Get specific medicine"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM medicines WHERE medicine_id = ?', (medicine_id,))
            medicine = cursor.fetchone()
            conn.close()
            
            return dict(medicine) if medicine else None
        except Exception as e:
            print(f"Error fetching medicine: {str(e)}")
            return None
    
    def update_medicine(self, medicine_id, medicine_name, quantity, price, expiry_date, manufacturer="", description=""):
        """Update medicine"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                UPDATE medicines 
                SET medicine_name = ?, quantity = ?, price = ?, expiry_date = ?, 
                    manufacturer = ?, description = ?, updated_at = CURRENT_TIMESTAMP
                WHERE medicine_id = ?
            ''', (medicine_name, quantity, price, expiry_date, manufacturer, description, medicine_id))
            
            conn.commit()
            conn.close()
            return True, "Medicine updated successfully"
        except Exception as e:
            return False, f"Error updating medicine: {str(e)}"
    
    def delete_medicine(self, medicine_id):
        """Delete medicine"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('DELETE FROM medicines WHERE medicine_id = ?', (medicine_id,))
            
            conn.commit()
            conn.close()
            return True, "Medicine deleted successfully"
        except Exception as e:
            return False, f"Error deleting medicine: {str(e)}"
    
    # Billing operations
    def add_bill(self, patient_id, amount, payment_method, bill_date, status="pending", notes=""):
        """Add new bill"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO billing (patient_id, amount, payment_method, bill_date, status, notes)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (patient_id, amount, payment_method, bill_date, status, notes))
            
            conn.commit()
            conn.close()
            return True, "Bill created successfully"
        except Exception as e:
            return False, f"Error creating bill: {str(e)}"
    
    def get_all_bills(self):
        """Get all bills"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM billing ORDER BY bill_date DESC')
            bills = cursor.fetchall()
            conn.close()
            
            return [dict(bill) for bill in bills]
        except Exception as e:
            print(f"Error fetching bills: {str(e)}")
            return []
    
    def get_bill(self, bill_id):
        """Get specific bill"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM billing WHERE bill_id = ?', (bill_id,))
            bill = cursor.fetchone()
            conn.close()
            
            return dict(bill) if bill else None
        except Exception as e:
            print(f"Error fetching bill: {str(e)}")
            return None
    
    def update_bill(self, bill_id, patient_id, amount, payment_method, bill_date, status="pending", notes=""):
        """Update bill"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                UPDATE billing 
                SET patient_id = ?, amount = ?, payment_method = ?, bill_date = ?, status = ?, notes = ?
                WHERE bill_id = ?
            ''', (patient_id, amount, payment_method, bill_date, status, notes, bill_id))
            
            conn.commit()
            conn.close()
            return True, "Bill updated successfully"
        except Exception as e:
            return False, f"Error updating bill: {str(e)}"
    
    def delete_bill(self, bill_id):
        """Delete bill"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('DELETE FROM billing WHERE bill_id = ?', (bill_id,))
            
            conn.commit()
            conn.close()
            return True, "Bill deleted successfully"
        except Exception as e:
            return False, f"Error deleting bill: {str(e)}"
    
    # Statistics
    def get_total_patients(self):
        """Get total number of patients"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT COUNT(*) as count FROM patients')
            result = cursor.fetchone()
            conn.close()
            return result['count'] if result else 0
        except Exception as e:
            print(f"Error: {str(e)}")
            return 0
    
    def get_total_doctors(self):
        """Get total number of doctors"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT COUNT(*) as count FROM doctors')
            result = cursor.fetchone()
            conn.close()
            return result['count'] if result else 0
        except Exception as e:
            print(f"Error: {str(e)}")
            return 0
    
    def get_total_appointments(self):
        """Get total number of appointments"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT COUNT(*) as count FROM appointments')
            result = cursor.fetchone()
            conn.close()
            return result['count'] if result else 0
        except Exception as e:
            print(f"Error: {str(e)}")
            return 0
    
    def get_total_revenue(self):
        """Get total revenue from billing"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT SUM(amount) as total FROM billing WHERE status = "completed"')
            result = cursor.fetchone()
            conn.close()
            return result['total'] if result and result['total'] else 0
        except Exception as e:
            print(f"Error: {str(e)}")
            return 0
