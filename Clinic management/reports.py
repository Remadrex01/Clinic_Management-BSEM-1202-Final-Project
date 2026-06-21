"""
Reports Module for Clinic Management System
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class ReportsManager:
    """Reports management class"""
    
    def __init__(self, parent, db):
        """Initialize reports manager"""
        self.parent = parent
        self.db = db
        
        self.setup_styles()
        self.create_ui()
    
    def setup_styles(self):
        """Setup styles"""
        self.bg_color = "#F5F5F5"
        self.primary_color = "#5B9BD5"
        self.text_color = "#2C3E50"
        self.success_color = "#27AE60"
        self.warning_color = "#E74C3C"
    
    def create_ui(self):
        """Create reports UI"""
        # Title
        title = tk.Label(self.parent, text="Reports & Analytics", 
                        font=("Segoe UI", 16, "bold"), fg=self.text_color,
                        bg=self.bg_color)
        title.pack(anchor=tk.W, pady=(0, 20))
        
        # Buttons frame
        buttons_frame = tk.Frame(self.parent, bg=self.bg_color)
        buttons_frame.pack(fill=tk.X, pady=(0, 20))
        
        patients_btn = tk.Button(buttons_frame, text="📊 Patient Report",
                                font=("Segoe UI", 9, "bold"),
                                bg=self.primary_color, fg="white",
                                cursor="hand2", command=self.show_patient_report,
                                padx=10, pady=5, relief=tk.FLAT, bd=0)
        patients_btn.pack(side=tk.LEFT, padx=5)
        
        doctors_btn = tk.Button(buttons_frame, text="📊 Doctor Report",
                               font=("Segoe UI", 9, "bold"),
                               bg=self.primary_color, fg="white",
                               cursor="hand2", command=self.show_doctor_report,
                               padx=10, pady=5, relief=tk.FLAT, bd=0)
        doctors_btn.pack(side=tk.LEFT, padx=5)
        
        appt_btn = tk.Button(buttons_frame, text="📊 Appointment Report",
                            font=("Segoe UI", 9, "bold"),
                            bg=self.primary_color, fg="white",
                            cursor="hand2", command=self.show_appointment_report,
                            padx=10, pady=5, relief=tk.FLAT, bd=0)
        appt_btn.pack(side=tk.LEFT, padx=5)
        
        revenue_btn = tk.Button(buttons_frame, text="📊 Revenue Report",
                               font=("Segoe UI", 9, "bold"),
                               bg=self.success_color, fg="white",
                               cursor="hand2", command=self.show_revenue_report,
                               padx=10, pady=5, relief=tk.FLAT, bd=0)
        revenue_btn.pack(side=tk.LEFT, padx=5)
        
        # Content frame
        self.content_frame = tk.Frame(self.parent, bg="white", relief=tk.FLAT, bd=1)
        self.content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Show dashboard by default
        self.show_summary()
    
    def clear_content(self):
        """Clear content frame"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def show_summary(self):
        """Show summary report"""
        self.clear_content()
        
        # Title
        title = tk.Label(self.content_frame, text="Clinic Summary", 
                        font=("Segoe UI", 14, "bold"), fg=self.text_color,
                        bg="white")
        title.pack(anchor=tk.W, padx=20, pady=(15, 20))
        
        # Summary frame
        summary_frame = tk.Frame(self.content_frame, bg="white")
        summary_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # Get data
        total_patients = self.db.get_total_patients()
        total_doctors = self.db.get_total_doctors()
        total_appointments = self.db.get_total_appointments()
        total_revenue = self.db.get_total_revenue()
        
        # Create summary labels
        summaries = [
            ("Total Patients", total_patients, self.primary_color),
            ("Total Doctors", total_doctors, self.success_color),
            ("Total Appointments", total_appointments, "#3498DB"),
            ("Total Revenue", f"₹{total_revenue:,.2f}", self.warning_color),
        ]
        
        for text, value, color in summaries:
            self.create_summary_card(summary_frame, text, value, color)
    
    def create_summary_card(self, parent, label, value, color):
        """Create summary card"""
        card = tk.Frame(parent, bg=color, relief=tk.FLAT, bd=0)
        card.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        content = tk.Frame(card, bg=color)
        content.pack(padx=15, pady=15, fill=tk.BOTH)
        
        label_text = tk.Label(content, text=label, font=("Segoe UI", 10),
                            fg="white", bg=color)
        label_text.pack(anchor=tk.W, pady=(0, 10))
        
        value_text = tk.Label(content, text=str(value), font=("Segoe UI", 20, "bold"),
                            fg="white", bg=color)
        value_text.pack(anchor=tk.W)
    
    def show_patient_report(self):
        """Show patient report"""
        self.clear_content()
        
        # Title
        title = tk.Label(self.content_frame, text="Patient Report", 
                        font=("Segoe UI", 14, "bold"), fg=self.text_color,
                        bg="white")
        title.pack(anchor=tk.W, padx=20, pady=(15, 20))
        
        # Create table
        columns = ("ID", "Name", "Age", "Gender", "Phone", "Address")
        tree = ttk.Treeview(self.content_frame, columns=columns, height=20, show="headings")
        
        for col in columns:
            tree.heading(col, text=col)
            if col == "ID":
                tree.column(col, width=50)
            elif col == "Name":
                tree.column(col, width=150)
            else:
                tree.column(col, width=120)
        
        # Get patients
        patients = self.db.get_all_patients()
        for patient in patients:
            tree.insert("", tk.END, values=(
                patient['patient_id'],
                patient['full_name'],
                patient['age'],
                patient['gender'],
                patient['phone'],
                patient['address']
            ))
        
        tree.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Footer
        footer = tk.Label(self.content_frame, 
                         text=f"Total Patients: {len(patients)}", 
                         font=("Segoe UI", 10), fg=self.text_color,
                         bg="white")
        footer.pack(padx=20, pady=15)
    
    def show_doctor_report(self):
        """Show doctor report"""
        self.clear_content()
        
        # Title
        title = tk.Label(self.content_frame, text="Doctor Report", 
                        font=("Segoe UI", 14, "bold"), fg=self.text_color,
                        bg="white")
        title.pack(anchor=tk.W, padx=20, pady=(15, 20))
        
        # Create table
        columns = ("ID", "Name", "Specialization", "Phone", "Email", "Experience")
        tree = ttk.Treeview(self.content_frame, columns=columns, height=20, show="headings")
        
        for col in columns:
            tree.heading(col, text=col)
            if col == "ID":
                tree.column(col, width=50)
            elif col == "Name":
                tree.column(col, width=120)
            else:
                tree.column(col, width=110)
        
        # Get doctors
        doctors = self.db.get_all_doctors()
        for doctor in doctors:
            tree.insert("", tk.END, values=(
                doctor['doctor_id'],
                doctor['name'],
                doctor['specialization'],
                doctor['phone'],
                doctor['email'],
                f"{doctor['experience_years']} years"
            ))
        
        tree.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Footer
        footer = tk.Label(self.content_frame, 
                         text=f"Total Doctors: {len(doctors)}", 
                         font=("Segoe UI", 10), fg=self.text_color,
                         bg="white")
        footer.pack(padx=20, pady=15)
    
    def show_appointment_report(self):
        """Show appointment report"""
        self.clear_content()
        
        # Title
        title = tk.Label(self.content_frame, text="Appointment Report", 
                        font=("Segoe UI", 14, "bold"), fg=self.text_color,
                        bg="white")
        title.pack(anchor=tk.W, padx=20, pady=(15, 20))
        
        # Create table
        columns = ("ID", "Patient", "Doctor", "Date", "Time", "Status")
        tree = ttk.Treeview(self.content_frame, columns=columns, height=20, show="headings")
        
        for col in columns:
            tree.heading(col, text=col)
            if col == "ID":
                tree.column(col, width=50)
            else:
                tree.column(col, width=140)
        
        # Get appointments
        appointments = self.db.get_all_appointments()
        for appt in appointments:
            patient = self.db.get_patient(appt['patient_id'])
            doctor = self.db.get_doctor(appt['doctor_id'])
            
            patient_name = patient['full_name'] if patient else "Unknown"
            doctor_name = doctor['name'] if doctor else "Unknown"
            
            tree.insert("", tk.END, values=(
                appt['appointment_id'],
                patient_name,
                doctor_name,
                appt['appointment_date'],
                appt['appointment_time'],
                appt['status']
            ))
        
        tree.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Footer
        footer = tk.Label(self.content_frame, 
                         text=f"Total Appointments: {len(appointments)}", 
                         font=("Segoe UI", 10), fg=self.text_color,
                         bg="white")
        footer.pack(padx=20, pady=15)
    
    def show_revenue_report(self):
        """Show revenue report"""
        self.clear_content()
        
        # Title
        title = tk.Label(self.content_frame, text="Revenue Report", 
                        font=("Segoe UI", 14, "bold"), fg=self.text_color,
                        bg="white")
        title.pack(anchor=tk.W, padx=20, pady=(15, 20))
        
        # Create table
        columns = ("ID", "Patient", "Amount", "Payment Method", "Status", "Date")
        tree = ttk.Treeview(self.content_frame, columns=columns, height=20, show="headings")
        
        for col in columns:
            tree.heading(col, text=col)
            if col == "ID":
                tree.column(col, width=50)
            elif col == "Patient":
                tree.column(col, width=130)
            else:
                tree.column(col, width=110)
        
        # Get bills
        bills = self.db.get_all_bills()
        total_revenue = 0
        completed_revenue = 0
        
        for bill in bills:
            patient = self.db.get_patient(bill['patient_id'])
            patient_name = patient['full_name'] if patient else "Unknown"
            
            tree.insert("", tk.END, values=(
                bill['bill_id'],
                patient_name,
                f"₹{bill['amount']:.2f}",
                bill['payment_method'],
                bill['status'],
                bill['bill_date']
            ))
            
            total_revenue += bill['amount']
            if bill['status'] == "completed":
                completed_revenue += bill['amount']
        
        tree.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Footer
        footer_text = f"Total Revenue: ₹{total_revenue:,.2f} | Completed: ₹{completed_revenue:,.2f} | Total Bills: {len(bills)}"
        footer = tk.Label(self.content_frame, 
                         text=footer_text, 
                         font=("Segoe UI", 10, "bold"), fg=self.text_color,
                         bg="white")
        footer.pack(padx=20, pady=15)
