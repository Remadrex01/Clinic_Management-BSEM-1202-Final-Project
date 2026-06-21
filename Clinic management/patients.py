"""
Patient Management Module for Clinic Management System
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime


class PatientManager:
    """Patient management class"""
    
    def __init__(self, parent, db):
        """Initialize patient manager"""
        self.parent = parent
        self.db = db
        self.selected_patient = None
        
        self.setup_styles()
        self.create_ui()
        self.load_patients()
    
    def setup_styles(self):
        """Setup styles"""
        self.bg_color = "#F5F5F5"
        self.primary_color = "#5B9BD5"
        self.text_color = "#2C3E50"
        self.success_color = "#27AE60"
        self.warning_color = "#E74C3C"
    
    def create_ui(self):
        """Create patient management UI"""
        # Title
        title = tk.Label(self.parent, text="Patient Management", 
                        font=("Segoe UI", 16, "bold"), fg=self.text_color,
                        bg=self.bg_color)
        title.pack(anchor=tk.W, pady=(0, 20))
        
        # Search frame
        search_frame = tk.Frame(self.parent, bg="white", relief=tk.FLAT, bd=1)
        search_frame.pack(fill=tk.X, pady=(0, 15))
        
        search_label = tk.Label(search_frame, text="Search Patient:", 
                               font=("Segoe UI", 9), fg=self.text_color, bg="white")
        search_label.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var, 
                                width=30, font=("Segoe UI", 9))
        search_entry.pack(side=tk.LEFT, padx=5, pady=10)
        search_entry.bind("<KeyRelease>", lambda e: self.search_patients())
        
        # Buttons frame
        buttons_frame = tk.Frame(self.parent, bg=self.bg_color)
        buttons_frame.pack(fill=tk.X, pady=(0, 15))
        
        add_btn = tk.Button(buttons_frame, text="➕ Add Patient",
                           font=("Segoe UI", 9, "bold"),
                           bg=self.success_color, fg="white",
                           cursor="hand2", command=self.add_patient,
                           padx=10, pady=5, relief=tk.FLAT, bd=0)
        add_btn.pack(side=tk.LEFT, padx=5)
        
        edit_btn = tk.Button(buttons_frame, text="✏️ Edit Patient",
                            font=("Segoe UI", 9, "bold"),
                            bg=self.primary_color, fg="white",
                            cursor="hand2", command=self.edit_patient,
                            padx=10, pady=5, relief=tk.FLAT, bd=0)
        edit_btn.pack(side=tk.LEFT, padx=5)
        
        delete_btn = tk.Button(buttons_frame, text="🗑️ Delete Patient",
                             font=("Segoe UI", 9, "bold"),
                             bg=self.warning_color, fg="white",
                             cursor="hand2", command=self.delete_patient,
                             padx=10, pady=5, relief=tk.FLAT, bd=0)
        delete_btn.pack(side=tk.LEFT, padx=5)
        
        # Table frame
        table_frame = tk.LabelFrame(self.parent, text="Patient List",
                                   font=("Segoe UI", 10, "bold"),
                                   fg=self.text_color, bg=self.bg_color,
                                   relief=tk.FLAT, bd=1)
        table_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create treeview
        columns = ("ID", "Name", "Age", "Gender", "Phone", "Address")
        self.tree = ttk.Treeview(table_frame, columns=columns, height=20, show="headings")
        
        for col in columns:
            self.tree.heading(col, text=col)
            if col == "ID":
                self.tree.column(col, width=50)
            elif col == "Name":
                self.tree.column(col, width=150)
            else:
                self.tree.column(col, width=120)
        
        # Scrollbars
        vsb = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        hsb = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscroll=vsb.set, xscroll=hsb.set)
        
        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")
        
        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)
        
        self.tree.bind("<Double-1>", lambda e: self.edit_patient())
    
    def load_patients(self):
        """Load patients into table"""
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Load patients
        patients = self.db.get_all_patients()
        
        for patient in patients:
            self.tree.insert("", tk.END, values=(
                patient['patient_id'],
                patient['full_name'],
                patient['age'],
                patient['gender'],
                patient['phone'],
                patient['address']
            ))
    
    def search_patients(self):
        """Search patients"""
        search_term = self.search_var.get()
        
        if not search_term:
            self.load_patients()
            return
        
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Search
        patients = self.db.search_patients(search_term)
        
        for patient in patients:
            self.tree.insert("", tk.END, values=(
                patient['patient_id'],
                patient['full_name'],
                patient['age'],
                patient['gender'],
                patient['phone'],
                patient['address']
            ))
    
    def get_selected_patient(self):
        """Get selected patient"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a patient")
            return None
        
        item = self.tree.item(selection[0])
        return item['values'][0]
    
    def add_patient(self):
        """Add new patient"""
        window = tk.Toplevel(self.parent)
        window.title("Add Patient")
        window.geometry("500x600")
        window.resizable(False, False)
        
        # Frame
        frame = tk.Frame(window, bg="white")
        frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Full Name
        tk.Label(frame, text="Full Name:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        fullname_var = tk.StringVar()
        ttk.Entry(frame, textvariable=fullname_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Age
        tk.Label(frame, text="Age:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        age_var = tk.StringVar()
        ttk.Entry(frame, textvariable=age_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Gender
        tk.Label(frame, text="Gender:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        gender_var = tk.StringVar()
        gender_combo = ttk.Combobox(frame, textvariable=gender_var, 
                                   values=["Male", "Female", "Other"],
                                   font=("Segoe UI", 9), width=37, state="readonly")
        gender_combo.pack(fill=tk.X, pady=(0, 10))
        
        # Phone
        tk.Label(frame, text="Phone Number:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        phone_var = tk.StringVar()
        ttk.Entry(frame, textvariable=phone_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Address
        tk.Label(frame, text="Address:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        address_var = tk.StringVar()
        ttk.Entry(frame, textvariable=address_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Email
        tk.Label(frame, text="Email:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        email_var = tk.StringVar()
        ttk.Entry(frame, textvariable=email_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Blood Group
        tk.Label(frame, text="Blood Group:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        blood_var = tk.StringVar()
        blood_combo = ttk.Combobox(frame, textvariable=blood_var,
                                  values=["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"],
                                  font=("Segoe UI", 9), width=37, state="readonly")
        blood_combo.pack(fill=tk.X, pady=(0, 10))
        
        # Medical History
        tk.Label(frame, text="Medical History:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        history_var = tk.StringVar()
        ttk.Entry(frame, textvariable=history_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 20))
        
        # Save button
        def save():
            try:
                age = int(age_var.get()) if age_var.get() else 0
            except:
                messagebox.showerror("Error", "Age must be a number")
                return
            
            success, message = self.db.add_patient(
                fullname_var.get(),
                age,
                gender_var.get(),
                phone_var.get(),
                address_var.get(),
                email_var.get(),
                blood_var.get(),
                history_var.get()
            )
            
            if success:
                messagebox.showinfo("Success", message)
                self.load_patients()
                window.destroy()
            else:
                messagebox.showerror("Error", message)
        
        tk.Button(frame, text="Save", font=("Segoe UI", 10, "bold"),
                 bg=self.success_color, fg="white",
                 command=save, padx=20, pady=8, relief=tk.FLAT, bd=0).pack(pady=20)
    
    def edit_patient(self):
        """Edit selected patient"""
        patient_id = self.get_selected_patient()
        if not patient_id:
            return
        
        patient = self.db.get_patient(patient_id)
        if not patient:
            messagebox.showerror("Error", "Could not load patient")
            return
        
        window = tk.Toplevel(self.parent)
        window.title("Edit Patient")
        window.geometry("500x600")
        window.resizable(False, False)
        
        # Frame
        frame = tk.Frame(window, bg="white")
        frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Full Name
        tk.Label(frame, text="Full Name:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        fullname_var = tk.StringVar(value=patient['full_name'])
        ttk.Entry(frame, textvariable=fullname_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Age
        tk.Label(frame, text="Age:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        age_var = tk.StringVar(value=patient['age'] or "")
        ttk.Entry(frame, textvariable=age_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Gender
        tk.Label(frame, text="Gender:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        gender_var = tk.StringVar(value=patient['gender'] or "")
        gender_combo = ttk.Combobox(frame, textvariable=gender_var,
                                   values=["Male", "Female", "Other"],
                                   font=("Segoe UI", 9), width=37, state="readonly")
        gender_combo.pack(fill=tk.X, pady=(0, 10))
        
        # Phone
        tk.Label(frame, text="Phone Number:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        phone_var = tk.StringVar(value=patient['phone'])
        ttk.Entry(frame, textvariable=phone_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Address
        tk.Label(frame, text="Address:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        address_var = tk.StringVar(value=patient['address'])
        ttk.Entry(frame, textvariable=address_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Email
        tk.Label(frame, text="Email:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        email_var = tk.StringVar(value=patient['email'] or "")
        ttk.Entry(frame, textvariable=email_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Blood Group
        tk.Label(frame, text="Blood Group:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        blood_var = tk.StringVar(value=patient['blood_group'] or "")
        blood_combo = ttk.Combobox(frame, textvariable=blood_var,
                                  values=["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"],
                                  font=("Segoe UI", 9), width=37, state="readonly")
        blood_combo.pack(fill=tk.X, pady=(0, 10))
        
        # Medical History
        tk.Label(frame, text="Medical History:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        history_var = tk.StringVar(value=patient['medical_history'] or "")
        ttk.Entry(frame, textvariable=history_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 20))
        
        # Save button
        def save():
            try:
                age = int(age_var.get()) if age_var.get() else 0
            except:
                messagebox.showerror("Error", "Age must be a number")
                return
            
            success, message = self.db.update_patient(
                patient_id,
                fullname_var.get(),
                age,
                gender_var.get(),
                phone_var.get(),
                address_var.get(),
                email_var.get(),
                blood_var.get(),
                history_var.get()
            )
            
            if success:
                messagebox.showinfo("Success", message)
                self.load_patients()
                window.destroy()
            else:
                messagebox.showerror("Error", message)
        
        tk.Button(frame, text="Update", font=("Segoe UI", 10, "bold"),
                 bg=self.primary_color, fg="white",
                 command=save, padx=20, pady=8, relief=tk.FLAT, bd=0).pack(pady=20)
    
    def delete_patient(self):
        """Delete selected patient"""
        patient_id = self.get_selected_patient()
        if not patient_id:
            return
        
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this patient?"):
            success, message = self.db.delete_patient(patient_id)
            
            if success:
                messagebox.showinfo("Success", message)
                self.load_patients()
            else:
                messagebox.showerror("Error", message)
