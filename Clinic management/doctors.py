"""
Doctor Management Module for Clinic Management System
"""

import tkinter as tk
from tkinter import ttk, messagebox


class DoctorManager:
    """Doctor management class"""
    
    def __init__(self, parent, db):
        """Initialize doctor manager"""
        self.parent = parent
        self.db = db
        
        self.setup_styles()
        self.create_ui()
        self.load_doctors()
    
    def setup_styles(self):
        """Setup styles"""
        self.bg_color = "#F5F5F5"
        self.primary_color = "#5B9BD5"
        self.text_color = "#2C3E50"
        self.success_color = "#27AE60"
        self.warning_color = "#E74C3C"
    
    def create_ui(self):
        """Create doctor management UI"""
        # Title
        title = tk.Label(self.parent, text="Doctor Management", 
                        font=("Segoe UI", 16, "bold"), fg=self.text_color,
                        bg=self.bg_color)
        title.pack(anchor=tk.W, pady=(0, 20))
        
        # Search frame
        search_frame = tk.Frame(self.parent, bg="white", relief=tk.FLAT, bd=1)
        search_frame.pack(fill=tk.X, pady=(0, 15))
        
        search_label = tk.Label(search_frame, text="Search Doctor:", 
                               font=("Segoe UI", 9), fg=self.text_color, bg="white")
        search_label.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var, 
                                width=30, font=("Segoe UI", 9))
        search_entry.pack(side=tk.LEFT, padx=5, pady=10)
        search_entry.bind("<KeyRelease>", lambda e: self.search_doctors())
        
        # Buttons frame
        buttons_frame = tk.Frame(self.parent, bg=self.bg_color)
        buttons_frame.pack(fill=tk.X, pady=(0, 15))
        
        add_btn = tk.Button(buttons_frame, text="➕ Add Doctor",
                           font=("Segoe UI", 9, "bold"),
                           bg=self.success_color, fg="white",
                           cursor="hand2", command=self.add_doctor,
                           padx=10, pady=5, relief=tk.FLAT, bd=0)
        add_btn.pack(side=tk.LEFT, padx=5)
        
        edit_btn = tk.Button(buttons_frame, text="✏️ Edit Doctor",
                            font=("Segoe UI", 9, "bold"),
                            bg=self.primary_color, fg="white",
                            cursor="hand2", command=self.edit_doctor,
                            padx=10, pady=5, relief=tk.FLAT, bd=0)
        edit_btn.pack(side=tk.LEFT, padx=5)
        
        delete_btn = tk.Button(buttons_frame, text="🗑️ Delete Doctor",
                             font=("Segoe UI", 9, "bold"),
                             bg=self.warning_color, fg="white",
                             cursor="hand2", command=self.delete_doctor,
                             padx=10, pady=5, relief=tk.FLAT, bd=0)
        delete_btn.pack(side=tk.LEFT, padx=5)
        
        # Table frame
        table_frame = tk.LabelFrame(self.parent, text="Doctor List",
                                   font=("Segoe UI", 10, "bold"),
                                   fg=self.text_color, bg=self.bg_color,
                                   relief=tk.FLAT, bd=1)
        table_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create treeview
        columns = ("ID", "Name", "Specialization", "Phone", "Email")
        self.tree = ttk.Treeview(table_frame, columns=columns, height=20, show="headings")
        
        for col in columns:
            self.tree.heading(col, text=col)
            if col == "ID":
                self.tree.column(col, width=50)
            elif col == "Name":
                self.tree.column(col, width=150)
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
        
        self.tree.bind("<Double-1>", lambda e: self.edit_doctor())
    
    def load_doctors(self):
        """Load doctors into table"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        doctors = self.db.get_all_doctors()
        
        for doctor in doctors:
            self.tree.insert("", tk.END, values=(
                doctor['doctor_id'],
                doctor['name'],
                doctor['specialization'],
                doctor['phone'],
                doctor['email']
            ))
    
    def search_doctors(self):
        """Search doctors"""
        search_term = self.search_var.get()
        
        if not search_term:
            self.load_doctors()
            return
        
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        doctors = self.db.search_doctors(search_term)
        
        for doctor in doctors:
            self.tree.insert("", tk.END, values=(
                doctor['doctor_id'],
                doctor['name'],
                doctor['specialization'],
                doctor['phone'],
                doctor['email']
            ))
    
    def get_selected_doctor(self):
        """Get selected doctor"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a doctor")
            return None
        
        item = self.tree.item(selection[0])
        return item['values'][0]
    
    def add_doctor(self):
        """Add new doctor"""
        window = tk.Toplevel(self.parent)
        window.title("Add Doctor")
        window.geometry("500x550")
        window.resizable(False, False)
        
        frame = tk.Frame(window, bg="white")
        frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Name
        tk.Label(frame, text="Name:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        name_var = tk.StringVar()
        ttk.Entry(frame, textvariable=name_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Specialization
        tk.Label(frame, text="Specialization:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        spec_var = tk.StringVar()
        spec_combo = ttk.Combobox(frame, textvariable=spec_var,
                                 values=["Cardiology", "Neurology", "Orthopedics", "Dermatology", 
                                        "Pediatrics", "General", "Surgery", "Psychiatry"],
                                 font=("Segoe UI", 9), width=37, state="readonly")
        spec_combo.pack(fill=tk.X, pady=(0, 10))
        
        # Phone
        tk.Label(frame, text="Phone Number:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        phone_var = tk.StringVar()
        ttk.Entry(frame, textvariable=phone_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Email
        tk.Label(frame, text="Email:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        email_var = tk.StringVar()
        ttk.Entry(frame, textvariable=email_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Qualification
        tk.Label(frame, text="Qualification:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        qual_var = tk.StringVar()
        ttk.Entry(frame, textvariable=qual_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Experience
        tk.Label(frame, text="Years of Experience:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        exp_var = tk.StringVar()
        ttk.Entry(frame, textvariable=exp_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Available Days
        tk.Label(frame, text="Available Days:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        avail_var = tk.StringVar()
        ttk.Entry(frame, textvariable=avail_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 20))
        
        def save():
            try:
                exp = int(exp_var.get()) if exp_var.get() else 0
            except:
                messagebox.showerror("Error", "Experience must be a number")
                return
            
            success, message = self.db.add_doctor(
                name_var.get(),
                spec_var.get(),
                phone_var.get(),
                email_var.get(),
                qual_var.get(),
                exp,
                avail_var.get()
            )
            
            if success:
                messagebox.showinfo("Success", message)
                self.load_doctors()
                window.destroy()
            else:
                messagebox.showerror("Error", message)
        
        tk.Button(frame, text="Save", font=("Segoe UI", 10, "bold"),
                 bg=self.success_color, fg="white",
                 command=save, padx=20, pady=8, relief=tk.FLAT, bd=0).pack(pady=20)
    
    def edit_doctor(self):
        """Edit selected doctor"""
        doctor_id = self.get_selected_doctor()
        if not doctor_id:
            return
        
        doctor = self.db.get_doctor(doctor_id)
        if not doctor:
            messagebox.showerror("Error", "Could not load doctor")
            return
        
        window = tk.Toplevel(self.parent)
        window.title("Edit Doctor")
        window.geometry("500x550")
        window.resizable(False, False)
        
        frame = tk.Frame(window, bg="white")
        frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Name
        tk.Label(frame, text="Name:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        name_var = tk.StringVar(value=doctor['name'])
        ttk.Entry(frame, textvariable=name_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Specialization
        tk.Label(frame, text="Specialization:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        spec_var = tk.StringVar(value=doctor['specialization'] or "")
        spec_combo = ttk.Combobox(frame, textvariable=spec_var,
                                 values=["Cardiology", "Neurology", "Orthopedics", "Dermatology",
                                        "Pediatrics", "General", "Surgery", "Psychiatry"],
                                 font=("Segoe UI", 9), width=37, state="readonly")
        spec_combo.pack(fill=tk.X, pady=(0, 10))
        
        # Phone
        tk.Label(frame, text="Phone Number:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        phone_var = tk.StringVar(value=doctor['phone'])
        ttk.Entry(frame, textvariable=phone_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Email
        tk.Label(frame, text="Email:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        email_var = tk.StringVar(value=doctor['email'])
        ttk.Entry(frame, textvariable=email_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Qualification
        tk.Label(frame, text="Qualification:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        qual_var = tk.StringVar(value=doctor['qualification'] or "")
        ttk.Entry(frame, textvariable=qual_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Experience
        tk.Label(frame, text="Years of Experience:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        exp_var = tk.StringVar(value=doctor['experience_years'] or "")
        ttk.Entry(frame, textvariable=exp_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Available Days
        tk.Label(frame, text="Available Days:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        avail_var = tk.StringVar(value=doctor['available_days'] or "")
        ttk.Entry(frame, textvariable=avail_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 20))
        
        def save():
            try:
                exp = int(exp_var.get()) if exp_var.get() else 0
            except:
                messagebox.showerror("Error", "Experience must be a number")
                return
            
            success, message = self.db.update_doctor(
                doctor_id,
                name_var.get(),
                spec_var.get(),
                phone_var.get(),
                email_var.get(),
                qual_var.get(),
                exp,
                avail_var.get()
            )
            
            if success:
                messagebox.showinfo("Success", message)
                self.load_doctors()
                window.destroy()
            else:
                messagebox.showerror("Error", message)
        
        tk.Button(frame, text="Update", font=("Segoe UI", 10, "bold"),
                 bg=self.primary_color, fg="white",
                 command=save, padx=20, pady=8, relief=tk.FLAT, bd=0).pack(pady=20)
    
    def delete_doctor(self):
        """Delete selected doctor"""
        doctor_id = self.get_selected_doctor()
        if not doctor_id:
            return
        
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this doctor?"):
            success, message = self.db.delete_doctor(doctor_id)
            
            if success:
                messagebox.showinfo("Success", message)
                self.load_doctors()
            else:
                messagebox.showerror("Error", message)
