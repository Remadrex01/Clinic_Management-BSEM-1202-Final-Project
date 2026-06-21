# Clinic Management System

A comprehensive, professional Clinic Management System built with Python Tkinter and SQLite. This system is designed for easy clinic/hospital operations management with a clean, modern interface.

## Features

### 1. **User Authentication**
- Secure login system with password hashing (SHA-256)
- User registration with validation
- Role-based access control
- Secure session management

### 2. **Patient Management**
- Add, edit, delete, and search patients
- Store patient information (name, age, gender, phone, address, email, blood group, medical history)
- Patient list view with sorting and filtering capabilities

### 3. **Doctor Management**
- Add, edit, delete, and search doctors
- Store doctor information (name, specialization, phone, email, qualification, experience)
- View doctor list with details

### 4. **Appointment Management**
- Book, edit, and cancel appointments
- Schedule appointments with patients and doctors
- Track appointment status (scheduled, completed, cancelled)
- Add notes to appointments

### 5. **Pharmacy Module**
- Manage medicine inventory
- Add, edit, and delete medicines
- Track quantity and expiry dates
- Store price and manufacturer information

### 6. **Billing Module**
- Create and manage bills
- Track payment methods (Cash, Card, UPI, Cheque)
- Monitor payment status (pending, completed, cancelled)
- Add notes to bills

### 7. **Reports & Analytics**
- Patient reports with complete details
- Doctor reports with specialization
- Appointment statistics and history
- Revenue reports and financial analytics
- Dashboard with key metrics

### 8. **Dashboard**
- Professional statistics cards showing:
  - Total patients
  - Total doctors
  - Total appointments
  - Total revenue
- Recent appointments overview
- Quick navigation to all modules

### 9. **Settings**
- User account information
- Application preferences
- System information
- Theme and font size options

## Project Structure

```
clinic_management/
│
├── main.py                 # Application entry point
├── database.py             # Database operations and schema
├── login.py                # Login interface
├── register.py             # Registration interface
├── dashboard.py            # Main dashboard with navigation
├── patients.py             # Patient management module
├── doctors.py              # Doctor management module
├── appointments.py         # Appointment management module
├── pharmacy.py             # Pharmacy inventory module
├── billing.py              # Billing and invoice module
├── reports.py              # Reports and analytics module
├── settings.py             # Settings and preferences
│
├── assets/
│ ├── icons/               # Application icons (if needed)
│ └── images/              # Application images (if needed)
│
└── database/
    └── clinic.db          # SQLite database file (created automatically)
```

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- No external dependencies required (uses only Python standard library)

### Step 1: Clone or Download
```bash
cd "path/to/Clinic management"
```

### Step 2: Run the Application
```bash
python main.py
```

The application will:
1. Create the database folder if it doesn't exist
2. Initialize all required tables in the SQLite database
3. Launch the login window

## Usage Guide

### First Time Setup

1. **Register an Account**
   - Click "Register Here" on the login page
   - Fill in your details:
     - Full Name
     - Username (unique)
     - Email (unique)
     - Phone Number
     - Password (minimum 6 characters)
   - Click "Register" button
   - You'll be redirected to login page

2. **Login**
   - Enter your username and password
   - Optional: Check "Remember Me" to auto-fill credentials next time
   - Optional: Check "Show Password" to see your password
   - Click "Login" button

### After Login

#### Dashboard
- View key statistics (patients, doctors, appointments, revenue)
- See recent appointments
- Access all modules from the sidebar

#### Patient Management
- **Add Patient**: Click "Add Patient" to register a new patient
- **View Patients**: All registered patients are shown in the table
- **Search**: Use the search box to find patients by name, phone, or ID
- **Edit Patient**: Double-click a patient or click "Edit Patient"
- **Delete Patient**: Select a patient and click "Delete Patient"

#### Doctor Management
- **Add Doctor**: Register a new doctor with specialization
- **View Doctors**: List of all doctors with their specializations
- **Search**: Find doctors by name or specialization
- **Edit Doctor**: Modify doctor information
- **Delete Doctor**: Remove doctor from system

#### Appointment Management
- **Book Appointment**: Schedule new appointments with date, time, and notes
- **View Appointments**: See all scheduled appointments
- **Edit Appointment**: Change appointment details or status
- **Cancel Appointment**: Remove or cancel appointments

#### Pharmacy Module
- **Add Medicine**: Add new medicines to inventory
- **Track Inventory**: Monitor quantity and expiry dates
- **Edit Medicine**: Update medicine information
- **Delete Medicine**: Remove expired or discontinued medicines

#### Billing Module
- **Create Bill**: Generate new bills for patients
- **Payment Tracking**: Track payment methods and status
- **Edit Bill**: Modify bill details
- **Delete Bill**: Remove bills if needed

#### Reports
- **Patient Report**: Complete patient database export
- **Doctor Report**: Doctor information and statistics
- **Appointment Report**: Full appointment history
- **Revenue Report**: Financial analytics and billing summary

#### Settings
- View your account information
- Customize application preferences
- View system information

### Sidebar Navigation
- 📊 Dashboard - Main dashboard
- 👥 Patients - Patient management
- 👨‍⚕️ Doctors - Doctor management
- 📅 Appointments - Appointment scheduling
- 💊 Pharmacy - Medicine inventory
- 💰 Billing - Patient billing
- 📈 Reports - Analytics and reports
- ⚙️ Settings - Preferences
- 🚪 Logout - Exit application

## Database Schema

### Users Table
- user_id (Primary Key)
- username (Unique)
- password (Hashed)
- full_name
- email (Unique)
- phone
- role
- created_at

### Patients Table
- patient_id (Primary Key)
- full_name
- age
- gender
- phone
- address
- email
- blood_group
- medical_history
- created_at
- updated_at

### Doctors Table
- doctor_id (Primary Key)
- name
- specialization
- phone
- email
- qualification
- experience_years
- available_days
- created_at
- updated_at

### Appointments Table
- appointment_id (Primary Key)
- patient_id (Foreign Key)
- doctor_id (Foreign Key)
- appointment_date
- appointment_time
- status
- notes
- created_at

### Medicines Table
- medicine_id (Primary Key)
- medicine_name
- quantity
- price
- expiry_date
- manufacturer
- description
- created_at
- updated_at

### Billing Table
- bill_id (Primary Key)
- patient_id (Foreign Key)
- amount
- payment_method
- status
- bill_date
- notes
- created_at

## Security Features

1. **Password Security**
   - Passwords are hashed using SHA-256
   - Never stored in plain text
   - Verified during login

2. **Data Validation**
   - Input validation for all forms
   - Error handling and user feedback
   - Database constraints and relationships

3. **User Session**
   - Secure user authentication
   - Session management
   - Logout functionality

## System Requirements

- **OS**: Windows, macOS, or Linux
- **RAM**: Minimum 512MB
- **Storage**: Minimum 50MB for application and database
- **Display**: 1024x768 minimum resolution

## Keyboard Shortcuts

- `Enter` - Submit form or button click
- `Tab` - Navigate between fields
- Double-click - Edit patient/doctor/medicine

## Tips & Best Practices

1. **Regular Backups**: Backup the `database/clinic.db` file regularly
2. **Data Entry**: Always verify information before saving
3. **Search**: Use search functionality to quickly find records
4. **Reports**: Generate reports regularly for business insights
5. **Password**: Keep your login credentials secure

## Troubleshooting

### Application Won't Start
- Ensure Python 3.7+ is installed
- Check if all Python files are in the correct directory
- Try running: `python main.py` from command prompt

### Database Errors
- Ensure `database/` folder exists
- Check disk space is available
- Try deleting `database/clinic.db` to reset (WARNING: This deletes all data)

### GUI Display Issues
- Increase screen resolution to minimum 1024x768
- Ensure Python Tkinter is installed

## Features for School Projects

This system is ideal for:
- ✅ School database projects
- ✅ Python learning and practice
- ✅ GUI application development
- ✅ Database design and management
- ✅ Software engineering concepts
- ✅ Complete working application example

## Code Quality

- **Object-Oriented Design**: Clean OOP structure
- **Modularity**: Separate modules for each feature
- **Error Handling**: Comprehensive exception handling
- **Documentation**: Well-commented code
- **Best Practices**: Follows Python conventions

## License

This project is open source and available for educational and personal use.

## Support & Contribution

For issues, suggestions, or improvements:
- Review the code and documentation
- Ensure all requirements are met
- Test thoroughly before deployment

## Version History

- **v1.0** - Initial release with all features
  - User authentication system
  - Patient management
  - Doctor management
  - Appointment scheduling
  - Pharmacy inventory
  - Billing system
  - Reports and analytics
  - Dashboard

---

**Developed as a complete clinic management solution using Python Tkinter and SQLite**

For more information, refer to the individual module documentation in each Python file.
