"""
Pharmacy Module for Clinic Management System
"""

import tkinter as tk
from tkinter import ttk, messagebox


class PharmacyManager:
    """Pharmacy management class"""
    
    def __init__(self, parent, db):
        """Initialize pharmacy manager"""
        self.parent = parent
        self.db = db
        
        self.setup_styles()
        self.create_ui()
        self.load_medicines()
    
    def setup_styles(self):
        """Setup styles"""
        self.bg_color = "#F5F5F5"
        self.primary_color = "#5B9BD5"
        self.text_color = "#2C3E50"
        self.success_color = "#27AE60"
        self.warning_color = "#E74C3C"
    
    def create_ui(self):
        """Create pharmacy UI"""
        # Title
        title = tk.Label(self.parent, text="Pharmacy Management", 
                        font=("Segoe UI", 16, "bold"), fg=self.text_color,
                        bg=self.bg_color)
        title.pack(anchor=tk.W, pady=(0, 20))
        
        # Search frame
        search_frame = tk.Frame(self.parent, bg="white", relief=tk.FLAT, bd=1)
        search_frame.pack(fill=tk.X, pady=(0, 15))
        
        search_label = tk.Label(search_frame, text="Search Medicine:", 
                               font=("Segoe UI", 9), fg=self.text_color, bg="white")
        search_label.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var, 
                                width=30, font=("Segoe UI", 9))
        search_entry.pack(side=tk.LEFT, padx=5, pady=10)
        search_entry.bind("<KeyRelease>", lambda e: self.search_medicines())
        
        # Buttons frame
        buttons_frame = tk.Frame(self.parent, bg=self.bg_color)
        buttons_frame.pack(fill=tk.X, pady=(0, 15))
        
        add_btn = tk.Button(buttons_frame, text="➕ Add Medicine",
                           font=("Segoe UI", 9, "bold"),
                           bg=self.success_color, fg="white",
                           cursor="hand2", command=self.add_medicine,
                           padx=10, pady=5, relief=tk.FLAT, bd=0)
        add_btn.pack(side=tk.LEFT, padx=5)
        
        edit_btn = tk.Button(buttons_frame, text="✏️ Edit Medicine",
                            font=("Segoe UI", 9, "bold"),
                            bg=self.primary_color, fg="white",
                            cursor="hand2", command=self.edit_medicine,
                            padx=10, pady=5, relief=tk.FLAT, bd=0)
        edit_btn.pack(side=tk.LEFT, padx=5)
        
        delete_btn = tk.Button(buttons_frame, text="🗑️ Delete Medicine",
                             font=("Segoe UI", 9, "bold"),
                             bg=self.warning_color, fg="white",
                             cursor="hand2", command=self.delete_medicine,
                             padx=10, pady=5, relief=tk.FLAT, bd=0)
        delete_btn.pack(side=tk.LEFT, padx=5)
        
        # Table frame
        table_frame = tk.LabelFrame(self.parent, text="Medicine Inventory",
                                   font=("Segoe UI", 10, "bold"),
                                   fg=self.text_color, bg=self.bg_color,
                                   relief=tk.FLAT, bd=1)
        table_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create treeview
        columns = ("ID", "Name", "Quantity", "Price", "Expiry Date", "Manufacturer")
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
    
    def load_medicines(self):
        """Load medicines into table"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        medicines = self.db.get_all_medicines()
        
        for med in medicines:
            self.tree.insert("", tk.END, values=(
                med['medicine_id'],
                med['medicine_name'],
                med['quantity'],
                f"₹{med['price']:.2f}" if med['price'] else "N/A",
                med['expiry_date'],
                med['manufacturer']
            ))
    
    def search_medicines(self):
        """Search medicines"""
        search_term = self.search_var.get()
        
        if not search_term:
            self.load_medicines()
            return
        
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        medicines = self.db.get_all_medicines()
        filtered = [m for m in medicines if search_term.lower() in m['medicine_name'].lower()]
        
        for med in filtered:
            self.tree.insert("", tk.END, values=(
                med['medicine_id'],
                med['medicine_name'],
                med['quantity'],
                f"₹{med['price']:.2f}" if med['price'] else "N/A",
                med['expiry_date'],
                med['manufacturer']
            ))
    
    def get_selected_medicine(self):
        """Get selected medicine"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a medicine")
            return None
        
        item = self.tree.item(selection[0])
        return item['values'][0]
    
    def add_medicine(self):
        """Add new medicine"""
        window = tk.Toplevel(self.parent)
        window.title("Add Medicine")
        window.geometry("500x550")
        window.resizable(False, False)
        
        frame = tk.Frame(window, bg="white")
        frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Medicine Name
        tk.Label(frame, text="Medicine Name:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        name_var = tk.StringVar()
        ttk.Entry(frame, textvariable=name_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Quantity
        tk.Label(frame, text="Quantity:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        qty_var = tk.StringVar()
        ttk.Entry(frame, textvariable=qty_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Price
        tk.Label(frame, text="Price (₹):", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        price_var = tk.StringVar()
        ttk.Entry(frame, textvariable=price_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Expiry Date
        tk.Label(frame, text="Expiry Date (YYYY-MM-DD):", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        expiry_var = tk.StringVar()
        ttk.Entry(frame, textvariable=expiry_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Manufacturer
        tk.Label(frame, text="Manufacturer:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        manuf_var = tk.StringVar()
        ttk.Entry(frame, textvariable=manuf_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Description
        tk.Label(frame, text="Description:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        desc_var = tk.StringVar()
        ttk.Entry(frame, textvariable=desc_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 20))
        
        def save():
            try:
                qty = int(qty_var.get()) if qty_var.get() else 0
                price = float(price_var.get()) if price_var.get() else 0.0
            except:
                messagebox.showerror("Error", "Quantity and Price must be numbers")
                return
            
            success, message = self.db.add_medicine(
                name_var.get(),
                qty,
                price,
                expiry_var.get(),
                manuf_var.get(),
                desc_var.get()
            )
            
            if success:
                messagebox.showinfo("Success", message)
                self.load_medicines()
                window.destroy()
            else:
                messagebox.showerror("Error", message)
        
        tk.Button(frame, text="Save", font=("Segoe UI", 10, "bold"),
                 bg=self.success_color, fg="white",
                 command=save, padx=20, pady=8, relief=tk.FLAT, bd=0).pack(pady=20)
    
    def edit_medicine(self):
        """Edit selected medicine"""
        med_id = self.get_selected_medicine()
        if not med_id:
            return
        
        med = self.db.get_medicine(med_id)
        if not med:
            messagebox.showerror("Error", "Could not load medicine")
            return
        
        window = tk.Toplevel(self.parent)
        window.title("Edit Medicine")
        window.geometry("500x550")
        window.resizable(False, False)
        
        frame = tk.Frame(window, bg="white")
        frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Medicine Name
        tk.Label(frame, text="Medicine Name:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        name_var = tk.StringVar(value=med['medicine_name'])
        ttk.Entry(frame, textvariable=name_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Quantity
        tk.Label(frame, text="Quantity:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        qty_var = tk.StringVar(value=med['quantity'] or "")
        ttk.Entry(frame, textvariable=qty_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Price
        tk.Label(frame, text="Price (₹):", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        price_var = tk.StringVar(value=med['price'] or "")
        ttk.Entry(frame, textvariable=price_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Expiry Date
        tk.Label(frame, text="Expiry Date (YYYY-MM-DD):", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        expiry_var = tk.StringVar(value=med['expiry_date'] or "")
        ttk.Entry(frame, textvariable=expiry_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Manufacturer
        tk.Label(frame, text="Manufacturer:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        manuf_var = tk.StringVar(value=med['manufacturer'] or "")
        ttk.Entry(frame, textvariable=manuf_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Description
        tk.Label(frame, text="Description:", font=("Segoe UI", 9, "bold"), bg="white").pack(anchor=tk.W, pady=(0, 5))
        desc_var = tk.StringVar(value=med['description'] or "")
        ttk.Entry(frame, textvariable=desc_var, font=("Segoe UI", 9), width=40).pack(fill=tk.X, pady=(0, 20))
        
        def save():
            try:
                qty = int(qty_var.get()) if qty_var.get() else 0
                price = float(price_var.get()) if price_var.get() else 0.0
            except:
                messagebox.showerror("Error", "Quantity and Price must be numbers")
                return
            
            success, message = self.db.update_medicine(
                med_id,
                name_var.get(),
                qty,
                price,
                expiry_var.get(),
                manuf_var.get(),
                desc_var.get()
            )
            
            if success:
                messagebox.showinfo("Success", message)
                self.load_medicines()
                window.destroy()
            else:
                messagebox.showerror("Error", message)
        
        tk.Button(frame, text="Update", font=("Segoe UI", 10, "bold"),
                 bg=self.primary_color, fg="white",
                 command=save, padx=20, pady=8, relief=tk.FLAT, bd=0).pack(pady=20)
    
    def delete_medicine(self):
        """Delete selected medicine"""
        med_id = self.get_selected_medicine()
        if not med_id:
            return
        
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this medicine?"):
            success, message = self.db.delete_medicine(med_id)
            
            if success:
                messagebox.showinfo("Success", message)
                self.load_medicines()
            else:
                messagebox.showerror("Error", message)
