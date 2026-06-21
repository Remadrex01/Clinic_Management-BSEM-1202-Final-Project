"""
Billing Module for Clinic Management System
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class BillingManager:
    """Billing management class"""
    
    def __init__(self, parent, db):
        """Initialize billing manager"""
        self.parent = parent
        self.db = db
        
        self.setup_styles()
        self.create_ui()
        self.load_bills()
    
    def setup_styles(self):
        """Setup styles"""
        self.bg_color = "#F5F5F5"
        self.primary_color = "#5B9BD5"
        self.text_color = "#2C3E50"
        self.success_color = "#27AE60"
        self.warning_color = "#E74C3C"
    
    def create_ui(self):
        """Create billing UI"""
        # Title
        title = tk.Label(self.parent, text="Billing Management", 
                        font=("Segoe UI", 16, "bold"), fg=self.text_color,
                        bg=self.bg_color)
        title.pack(anchor=tk.W, pady=(0, 20))
        
        # Buttons frame
        buttons_frame = tk.Frame(self.parent, bg=self.bg_color)
        buttons_frame.pack(fill=tk.X, pady=(0, 15))
        
        add_btn = tk.Button(buttons_frame, text="💰 Create Bill",
                           font=("Segoe UI", 9, "bold"),
                           bg=self.success_color, fg="white",
                           cursor="hand2", command=self.add_bill,
                           padx=10, pady=5, relief=tk.FLAT, bd=0)
        add_btn.pack(side=tk.LEFT, padx=5)
        
        edit_btn = tk.Button(buttons_frame, text="✏️ Edit Bill",
                            font=("Segoe UI", 9, "bold"),
                            bg=self.primary_color, fg="white",
                            cursor="hand2", command=self.edit_bill,
                            padx=10, pady=5, relief=tk.FLAT, bd=0)
        edit_btn.pack(side=tk.LEFT, padx=5)
        
        delete_btn = tk.Button(buttons_frame, text="🗑️ Delete Bill",
                             font=("Segoe UI", 9, "bold"),
                             bg=self.warning_color, fg="white",
                             cursor="hand2", command=self.delete_bill,
                             padx=10, pady=5, relief=tk.FLAT, bd=0)
        delete_btn.pack(side=tk.LEFT, padx=5)
        
        # Table frame
        table_frame = tk.LabelFrame(self.parent, text="Billing Records",
                                   font=("Segoe UI", 10, "bold"),
                                   fg=self.text_color, bg=self.bg_color,
                                   relief=tk.FLAT, bd=1)
        table_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create treeview
        columns = ("ID", "Patient", "Amount", "Payment Method", "Status", "Date")
        self.tree = ttk.Treeview(table_frame, columns=columns, height=20, show="headings")
        
        for col in columns:
            self.tree.heading(col, text=col)
            if col == "ID":
                self.tree.column(col, width=50)
            elif col == "Patient":
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
    
    def load_bills(self):
        """Load bills into table"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        bills = self.db.get_all_bills()
        
        for bill in bills:
            patient = self.db.get_patient(bill['patient_id'])
            patient_name = patient['full_name'] if patient else "Unknown"
            
            self.tree.insert("", tk.END, values=(
                bill['bill_id'],
                patient_name,
                f"₹{bill['amount']:.2f}",
                bill['payment_method'],
                bill['status'],
                bill['bill_date']
            ))
    
    def get_selected_bill(self):
        """Get selected bill"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a bill")
            return None
        
        item = self.tree.item(selection[0])
        return item['values'][0]
    
    def add_bill(self):
        """Add new bill"""
        window = tk.Toplevel(self.parent)
        window.title("Create Bill")
        window.geometry("500x500")
        window.resizable(False, False)
        
        frame = tk.Frame(window, bg="white")
        frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Get patients
        patients = self.db.get_all_patients()
        patient_names = [f"{p['patient_id']} - {p['full_name']}" for p in patients]
        
        # Patient
        tk.Label(frame, text="Select Patient:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        patient_var = tk.StringVar()
        patient_combo = ttk.Combobox(frame, textvariable=patient_var,
                                    values=patient_names,
                                    font=("Segoe UI", 9), width=40, state="readonly")
        patient_combo.pack(fill=tk.X, pady=(0, 10))
        
        # Amount
        tk.Label(frame, text="Amount (₹):", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        amount_var = tk.StringVar()
        ttk.Entry(frame, textvariable=amount_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Payment Method
        tk.Label(frame, text="Payment Method:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        payment_var = tk.StringVar()
        payment_combo = ttk.Combobox(frame, textvariable=payment_var,
                                    values=["Cash", "Credit Card", "Debit Card", "UPI", "Cheque"],
                                    font=("Segoe UI", 9), width=37, state="readonly")
        payment_combo.pack(fill=tk.X, pady=(0, 10))
        
        # Date
        tk.Label(frame, text="Bill Date (YYYY-MM-DD):", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        date_var = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))
        ttk.Entry(frame, textvariable=date_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Status
        tk.Label(frame, text="Status:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        status_var = tk.StringVar()
        status_combo = ttk.Combobox(frame, textvariable=status_var,
                                   values=["pending", "completed", "cancelled"],
                                   font=("Segoe UI", 9), width=37, state="readonly")
        status_combo.set("pending")
        status_combo.pack(fill=tk.X, pady=(0, 10))
        
        # Notes
        tk.Label(frame, text="Notes:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        notes_var = tk.StringVar()
        ttk.Entry(frame, textvariable=notes_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 20))
        
        def save():
            try:
                patient_id = int(patient_var.get().split(" - ")[0])
                amount = float(amount_var.get())
            except:
                messagebox.showerror("Error", "Please select patient and enter valid amount")
                return
            
            success, message = self.db.add_bill(
                patient_id,
                amount,
                payment_var.get(),
                date_var.get(),
                status_var.get(),
                notes_var.get()
            )
            
            if success:
                messagebox.showinfo("Success", message)
                self.load_bills()
                window.destroy()
            else:
                messagebox.showerror("Error", message)
        
        tk.Button(frame, text="Create", font=("Segoe UI", 10, "bold"),
                 bg=self.success_color, fg="white",
                 command=save, padx=20, pady=8, relief=tk.FLAT, bd=0).pack(pady=20)
    
    def edit_bill(self):
        """Edit selected bill"""
        bill_id = self.get_selected_bill()
        if not bill_id:
            return
        
        bill = self.db.get_bill(bill_id)
        if not bill:
            messagebox.showerror("Error", "Could not load bill")
            return
        
        window = tk.Toplevel(self.parent)
        window.title("Edit Bill")
        window.geometry("500x500")
        window.resizable(False, False)
        
        frame = tk.Frame(window, bg="white")
        frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Get patients
        patients = self.db.get_all_patients()
        patient_names = [f"{p['patient_id']} - {p['full_name']}" for p in patients]
        
        # Patient
        patient_obj = self.db.get_patient(bill['patient_id'])
        patient_display = f"{bill['patient_id']} - {patient_obj['full_name']}" if patient_obj else str(bill['patient_id'])
        
        tk.Label(frame, text="Select Patient:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        patient_var = tk.StringVar(value=patient_display)
        patient_combo = ttk.Combobox(frame, textvariable=patient_var,
                                    values=patient_names,
                                    font=("Segoe UI", 9), width=40, state="readonly")
        patient_combo.pack(fill=tk.X, pady=(0, 10))
        
        # Amount
        tk.Label(frame, text="Amount (₹):", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        amount_var = tk.StringVar(value=bill['amount'])
        ttk.Entry(frame, textvariable=amount_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Payment Method
        tk.Label(frame, text="Payment Method:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        payment_var = tk.StringVar(value=bill['payment_method'])
        payment_combo = ttk.Combobox(frame, textvariable=payment_var,
                                    values=["Cash", "Credit Card", "Debit Card", "UPI", "Cheque"],
                                    font=("Segoe UI", 9), width=37, state="readonly")
        payment_combo.pack(fill=tk.X, pady=(0, 10))
        
        # Date
        tk.Label(frame, text="Bill Date (YYYY-MM-DD):", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        date_var = tk.StringVar(value=bill['bill_date'])
        ttk.Entry(frame, textvariable=date_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Status
        tk.Label(frame, text="Status:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        status_var = tk.StringVar(value=bill['status'])
        status_combo = ttk.Combobox(frame, textvariable=status_var,
                                   values=["pending", "completed", "cancelled"],
                                   font=("Segoe UI", 9), width=37, state="readonly")
        status_combo.pack(fill=tk.X, pady=(0, 10))
        
        # Notes
        tk.Label(frame, text="Notes:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        notes_var = tk.StringVar(value=bill['notes'] or "")
        ttk.Entry(frame, textvariable=notes_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 20))
        
        def save():
            try:
                patient_id = int(patient_var.get().split(" - ")[0])
                amount = float(amount_var.get())
            except:
                messagebox.showerror("Error", "Please select patient and enter valid amount")
                return
            
            success, message = self.db.update_bill(
                bill_id,
                patient_id,
                amount,
                payment_var.get(),
                date_var.get(),
                status_var.get(),
                notes_var.get()
            )
            
            if success:
                messagebox.showinfo("Success", message)
                self.load_bills()
                window.destroy()
            else:
                messagebox.showerror("Error", message)
        
        tk.Button(frame, text="Update", font=("Segoe UI", 10, "bold"),
                 bg=self.primary_color, fg="white",
                 command=save, padx=20, pady=8, relief=tk.FLAT, bd=0).pack(pady=20)
    
    def delete_bill(self):
        """Delete selected bill"""
        bill_id = self.get_selected_bill()
        if not bill_id:
            return
        
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this bill?"):
            success, message = self.db.delete_bill(bill_id)
            
            if success:
                messagebox.showinfo("Success", message)
                self.load_bills()
            else:
                messagebox.showerror("Error", message)
