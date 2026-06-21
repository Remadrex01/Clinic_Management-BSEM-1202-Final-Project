"""
Appointment Management Module for Clinic Management System
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class AppointmentManager:
    """Appointment management class"""
    
    def __init__(self, parent, db):
        """Initialize appointment manager"""
        self.parent = parent
        self.db = db
        
        self.setup_styles()
        self.create_ui()
        self.load_appointments()
    
    def setup_styles(self):
        """Setup styles"""
        self.bg_color = "#F5F5F5"
        self.primary_color = "#5B9BD5"
        self.text_color = "#2C3E50"
        self.success_color = "#27AE60"
        self.warning_color = "#E74C3C"
    
    def create_ui(self):
        """Create appointment management UI"""
        # Title
        title = tk.Label(self.parent, text="Appointment Management", 
                        font=("Segoe UI", 16, "bold"), fg=self.text_color,
                        bg=self.bg_color)
        title.pack(anchor=tk.W, pady=(0, 20))
        
        # Buttons frame
        buttons_frame = tk.Frame(self.parent, bg=self.bg_color)
        buttons_frame.pack(fill=tk.X, pady=(0, 15))
        
        add_btn = tk.Button(buttons_frame, text="📅 Book Appointment",
                           font=("Segoe UI", 9, "bold"),
                           bg=self.success_color, fg="white",
                           cursor="hand2", command=self.add_appointment,
                           padx=10, pady=5, relief=tk.FLAT, bd=0)
        add_btn.pack(side=tk.LEFT, padx=5)
        
        edit_btn = tk.Button(buttons_frame, text="✏️ Edit Appointment",
                            font=("Segoe UI", 9, "bold"),
                            bg=self.primary_color, fg="white",
                            cursor="hand2", command=self.edit_appointment,
                            padx=10, pady=5, relief=tk.FLAT, bd=0)
        edit_btn.pack(side=tk.LEFT, padx=5)
        
        delete_btn = tk.Button(buttons_frame, text="❌ Cancel Appointment",
                             font=("Segoe UI", 9, "bold"),
                             bg=self.warning_color, fg="white",
                             cursor="hand2", command=self.delete_appointment,
                             padx=10, pady=5, relief=tk.FLAT, bd=0)
        delete_btn.pack(side=tk.LEFT, padx=5)
        
        # Table frame
        table_frame = tk.LabelFrame(self.parent, text="Appointment List",
                                   font=("Segoe UI", 10, "bold"),
                                   fg=self.text_color, bg=self.bg_color,
                                   relief=tk.FLAT, bd=1)
        table_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create treeview
        columns = ("ID", "Patient", "Doctor", "Date", "Time", "Status")
        self.tree = ttk.Treeview(table_frame, columns=columns, height=20, show="headings")
        
        for col in columns:
            self.tree.heading(col, text=col)
            if col == "ID":
                self.tree.column(col, width=50)
            else:
                self.tree.column(col, width=150)
        
        # Scrollbars
        vsb = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        hsb = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscroll=vsb.set, xscroll=hsb.set)
        
        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")
        
        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)
    
    def load_appointments(self):
        """Load appointments into table"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        appointments = self.db.get_all_appointments()
        
        for appt in appointments:
            patient = self.db.get_patient(appt['patient_id'])
            doctor = self.db.get_doctor(appt['doctor_id'])
            
            patient_name = patient['full_name'] if patient else "Unknown"
            doctor_name = doctor['name'] if doctor else "Unknown"
            
            self.tree.insert("", tk.END, values=(
                appt['appointment_id'],
                patient_name,
                doctor_name,
                appt['appointment_date'],
                appt['appointment_time'],
                appt['status']
            ))
    
    def get_selected_appointment(self):
        """Get selected appointment"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select an appointment")
            return None
        
        item = self.tree.item(selection[0])
        return item['values'][0]
    
    def add_appointment(self):
        """Add new appointment"""
        window = tk.Toplevel(self.parent)
        window.title("Book Appointment")
        window.geometry("500x500")
        window.resizable(False, False)
        
        frame = tk.Frame(window, bg="white")
        frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Get patients and doctors
        patients = self.db.get_all_patients()
        doctors = self.db.get_all_doctors()
        
        patient_names = [f"{p['patient_id']} - {p['full_name']}" for p in patients]
        doctor_names = [f"{d['doctor_id']} - {d['name']}" for d in doctors]
        
        # Patient
        tk.Label(frame, text="Select Patient:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        patient_var = tk.StringVar()
        patient_combo = ttk.Combobox(frame, textvariable=patient_var,
                                    values=patient_names,
                                    font=("Segoe UI", 9), width=40, state="readonly")
        patient_combo.pack(fill=tk.X, pady=(0, 10))
        
        # Doctor
        tk.Label(frame, text="Select Doctor:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        doctor_var = tk.StringVar()
        doctor_combo = ttk.Combobox(frame, textvariable=doctor_var,
                                   values=doctor_names,
                                   font=("Segoe UI", 9), width=40, state="readonly")
        doctor_combo.pack(fill=tk.X, pady=(0, 10))
        
        # Date
        tk.Label(frame, text="Date (YYYY-MM-DD):", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        date_var = tk.StringVar()
        ttk.Entry(frame, textvariable=date_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Time
        tk.Label(frame, text="Time (HH:MM):", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        time_var = tk.StringVar()
        ttk.Entry(frame, textvariable=time_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Status
        tk.Label(frame, text="Status:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        status_var = tk.StringVar()
        status_combo = ttk.Combobox(frame, textvariable=status_var,
                                   values=["scheduled", "completed", "cancelled"],
                                   font=("Segoe UI", 9), width=37, state="readonly")
        status_combo.set("scheduled")
        status_combo.pack(fill=tk.X, pady=(0, 10))
        
        # Notes
        tk.Label(frame, text="Notes:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        notes_var = tk.StringVar()
        ttk.Entry(frame, textvariable=notes_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 20))
        
        def save():
            try:
                patient_id = int(patient_var.get().split(" - ")[0])
                doctor_id = int(doctor_var.get().split(" - ")[0])
            except:
                messagebox.showerror("Error", "Please select patient and doctor")
                return
            
            if not date_var.get() or not time_var.get():
                messagebox.showerror("Error", "Please enter date and time")
                return
            
            success, message = self.db.add_appointment(
                patient_id,
                doctor_id,
                date_var.get(),
                time_var.get(),
                status_var.get(),
                notes_var.get()
            )
            
            if success:
                messagebox.showinfo("Success", message)
                self.load_appointments()
                window.destroy()
            else:
                messagebox.showerror("Error", message)
        
        tk.Button(frame, text="Book", font=("Segoe UI", 10, "bold"),
                 bg=self.success_color, fg="white",
                 command=save, padx=20, pady=8, relief=tk.FLAT, bd=0).pack(pady=20)
    
    def edit_appointment(self):
        """Edit selected appointment"""
        appt_id = self.get_selected_appointment()
        if not appt_id:
            return
        
        appt = self.db.get_appointment(appt_id)
        if not appt:
            messagebox.showerror("Error", "Could not load appointment")
            return
        
        window = tk.Toplevel(self.parent)
        window.title("Edit Appointment")
        window.geometry("500x500")
        window.resizable(False, False)
        
        frame = tk.Frame(window, bg="white")
        frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Get patients and doctors
        patients = self.db.get_all_patients()
        doctors = self.db.get_all_doctors()
        
        patient_names = [f"{p['patient_id']} - {p['full_name']}" for p in patients]
        doctor_names = [f"{d['doctor_id']} - {d['name']}" for d in doctors]
        
        # Patient
        tk.Label(frame, text="Select Patient:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        patient_var = tk.StringVar(value=f"{appt['patient_id']} - {self.db.get_patient(appt['patient_id'])['full_name']}")
        patient_combo = ttk.Combobox(frame, textvariable=patient_var,
                                    values=patient_names,
                                    font=("Segoe UI", 9), width=40, state="readonly")
        patient_combo.pack(fill=tk.X, pady=(0, 10))
        
        # Doctor
        tk.Label(frame, text="Select Doctor:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        doctor_var = tk.StringVar(value=f"{appt['doctor_id']} - {self.db.get_doctor(appt['doctor_id'])['name']}")
        doctor_combo = ttk.Combobox(frame, textvariable=doctor_var,
                                   values=doctor_names,
                                   font=("Segoe UI", 9), width=40, state="readonly")
        doctor_combo.pack(fill=tk.X, pady=(0, 10))
        
        # Date
        tk.Label(frame, text="Date (YYYY-MM-DD):", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        date_var = tk.StringVar(value=appt['appointment_date'])
        ttk.Entry(frame, textvariable=date_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Time
        tk.Label(frame, text="Time (HH:MM):", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        time_var = tk.StringVar(value=appt['appointment_time'])
        ttk.Entry(frame, textvariable=time_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Status
        tk.Label(frame, text="Status:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        status_var = tk.StringVar(value=appt['status'])
        status_combo = ttk.Combobox(frame, textvariable=status_var,
                                   values=["scheduled", "completed", "cancelled"],
                                   font=("Segoe UI", 9), width=37, state="readonly")
        status_combo.pack(fill=tk.X, pady=(0, 10))
        
        # Notes
        tk.Label(frame, text="Notes:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        notes_var = tk.StringVar(value=appt['notes'] or "")
        ttk.Entry(frame, textvariable=notes_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 20))
        
        def save():
            try:
                patient_id = int(patient_var.get().split(" - ")[0])
                doctor_id = int(doctor_var.get().split(" - ")[0])
            except:
                messagebox.showerror("Error", "Please select patient and doctor")
                return
            
            success, message = self.db.update_appointment(
                appt_id,
                patient_id,
                doctor_id,
                date_var.get(),
                time_var.get(),
                status_var.get(),
                notes_var.get()
            )
            
            if success:
                messagebox.showinfo("Success", message)
                self.load_appointments()
                window.destroy()
            else:
                messagebox.showerror("Error", message)
        
        tk.Button(frame, text="Update", font=("Segoe UI", 10, "bold"),
                 bg=self.primary_color, fg="white",
                 command=save, padx=20, pady=8, relief=tk.FLAT, bd=0).pack(pady=20)
    
    def delete_appointment(self):
        """Delete selected appointment"""
        appt_id = self.get_selected_appointment()
        if not appt_id:
            return
        
        if messagebox.askyesno("Confirm", "Are you sure you want to cancel this appointment?"):
            success, message = self.db.delete_appointment(appt_id)
            
            if success:
                messagebox.showinfo("Success", message)
                self.load_appointments()
            else:
                messagebox.showerror("Error", message)
