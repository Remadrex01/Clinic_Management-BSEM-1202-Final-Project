"""
Register Module for Clinic Management System
Handles user registration with email verification
"""

import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tkFont
import random
import string
from datetime import datetime, timedelta
from database import DatabaseManager


class RegisterWindow:
    """Registration window class"""
    
    def __init__(self, root, on_back_callback):
        """Initialize registration window"""
        self.root = root
        self.on_back_callback = on_back_callback
        self.db = DatabaseManager()
        
        # Configure window
        self.root.title("Clinic Management System - Register")
        self.root.geometry("900x750")
        self.root.resizable(False, False)
        
        # Center window on screen
        self.center_window()
        
        # Configure style
        self.setup_styles()
        
        # Create UI
        self.create_register_ui()
    
    def center_window(self):
        """Center window on screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def setup_styles(self):
        """Setup custom styles"""
        self.bg_color = "#FFFFFF"
        self.primary_color = "#5B9BD5"
        self.secondary_color = "#D4E6F1"
        self.text_color = "#2C3E50"
        self.border_color = "#BDC3C7"
        
        self.root.configure(bg=self.bg_color)
    
    def create_register_ui(self):
        """Create registration UI"""
        # Main container
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Center container for card
        center_frame = tk.Frame(main_frame, bg=self.bg_color)
        center_frame.pack(expand=True)
        
        # Registration card
        card_frame = tk.Frame(center_frame, bg=self.bg_color, relief=tk.FLAT, bd=0)
        card_frame.pack()
        
        # Shadow effect
        shadow = tk.Frame(card_frame, bg=self.border_color, width=400)
        shadow.pack(padx=2, pady=2, fill=tk.BOTH)
        
        # Main card content
        register_card = tk.Frame(shadow, bg=self.bg_color)
        register_card.pack(padx=2, pady=2, fill=tk.BOTH, expand=True)
        
        # Header section
        header_frame = tk.Frame(register_card, bg=self.primary_color)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Title
        title = tk.Label(header_frame, text="Create Account", 
                        font=("Segoe UI", 20, "bold"), 
                        fg="white", bg=self.primary_color)
        title.pack(pady=15)
        
        subtitle = tk.Label(header_frame, text="Join Our Clinic", 
                           font=("Segoe UI", 10), 
                           fg=self.secondary_color, bg=self.primary_color)
        subtitle.pack()
        
        # Content frame with scrolling capability
        content_frame = tk.Frame(register_card, bg=self.bg_color)
        content_frame.pack(padx=40, pady=20, fill=tk.BOTH, expand=True)
        
        # Full Name
        fullname_label = tk.Label(content_frame, text="Full Name", 
                                 font=("Segoe UI", 9, "bold"), 
                                 fg=self.text_color, bg=self.bg_color)
        fullname_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.fullname_var = tk.StringVar()
        fullname_entry = ttk.Entry(content_frame, textvariable=self.fullname_var, 
                                   width=35, font=("Segoe UI", 10))
        fullname_entry.pack(fill=tk.X, pady=(0, 15))
        
        # Username
        username_label = tk.Label(content_frame, text="Username", 
                                 font=("Segoe UI", 9, "bold"), 
                                 fg=self.text_color, bg=self.bg_color)
        username_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.username_var = tk.StringVar()
        username_entry = ttk.Entry(content_frame, textvariable=self.username_var, 
                                   width=35, font=("Segoe UI", 10))
        username_entry.pack(fill=tk.X, pady=(0, 15))
        
        # Email
        email_label = tk.Label(content_frame, text="Email", 
                              font=("Segoe UI", 9, "bold"), 
                              fg=self.text_color, bg=self.bg_color)
        email_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.email_var = tk.StringVar()
        email_entry = ttk.Entry(content_frame, textvariable=self.email_var, 
                               width=35, font=("Segoe UI", 10))
        email_entry.pack(fill=tk.X, pady=(0, 15))
        
        # Phone
        phone_label = tk.Label(content_frame, text="Phone Number", 
                              font=("Segoe UI", 9, "bold"), 
                              fg=self.text_color, bg=self.bg_color)
        phone_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.phone_var = tk.StringVar()
        phone_entry = ttk.Entry(content_frame, textvariable=self.phone_var, 
                               width=35, font=("Segoe UI", 10))
        phone_entry.pack(fill=tk.X, pady=(0, 15))
        
        # Password
        password_label = tk.Label(content_frame, text="Password", 
                                 font=("Segoe UI", 9, "bold"), 
                                 fg=self.text_color, bg=self.bg_color)
        password_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.password_var = tk.StringVar()
        password_entry = ttk.Entry(content_frame, textvariable=self.password_var, 
                                   show="•", width=35, font=("Segoe UI", 10))
        password_entry.pack(fill=tk.X, pady=(0, 15))
        
        # Confirm Password
        confirm_label = tk.Label(content_frame, text="Confirm Password", 
                                font=("Segoe UI", 9, "bold"), 
                                fg=self.text_color, bg=self.bg_color)
        confirm_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.confirm_var = tk.StringVar()
        confirm_entry = ttk.Entry(content_frame, textvariable=self.confirm_var, 
                                  show="•", width=35, font=("Segoe UI", 10))
        confirm_entry.pack(fill=tk.X, pady=(0, 20))
        
        # Button frame
        button_frame = tk.Frame(content_frame, bg=self.bg_color)
        button_frame.pack(fill=tk.X, pady=(10, 0))
        
        # Register button
        register_btn = tk.Button(button_frame, text="Create Account", 
                               font=("Segoe UI", 10, "bold"),
                               bg=self.primary_color, fg="white",
                               cursor="hand2", command=self.register,
                               padx=20, pady=8, relief=tk.FLAT, bd=0)
        register_btn.pack(side=tk.LEFT, padx=(0, 10), fill=tk.X, expand=True)
        
        # Back button
        back_btn = tk.Button(button_frame, text="Back to Login", 
                           font=("Segoe UI", 10, "bold"),
                           bg=self.secondary_color, fg=self.text_color,
                           cursor="hand2", command=self.back_to_login,
                           padx=20, pady=8, relief=tk.FLAT, bd=0)
        back_btn.pack(side=tk.LEFT, fill=tk.X, expand=True)
    
    def generate_verification_code(self):
        """Generate a 6-digit verification code"""
        return ''.join(random.choices(string.digits, k=6))
    
    def register(self):
        """Handle registration"""
        fullname = self.fullname_var.get().strip()
        username = self.username_var.get().strip()
        email = self.email_var.get().strip()
        phone = self.phone_var.get().strip()
        password = self.password_var.get()
        confirm = self.confirm_var.get()
        
        # Validation
        if not all([fullname, username, email, password, confirm]):
            messagebox.showerror("Error", "Please fill in all fields")
            return
        
        if password != confirm:
            messagebox.showerror("Error", "Passwords do not match")
            return
        
        if len(password) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters")
            return
        
        if "@" not in email:
            messagebox.showerror("Error", "Please enter a valid email")
            return
        
        # Register user
        success, message = self.db.register_user(username, password, fullname, email, phone)
        
        if success:
            # Generate verification code
            verification_code = self.generate_verification_code()
            
            # Create verification code in database (expires in 15 minutes)
            expires_at = (datetime.now() + timedelta(minutes=15)).strftime("%Y-%m-%d %H:%M:%S")
            code_success, code_message = self.db.create_verification_code(
                username, email, verification_code, expires_at
            )
            
            if code_success:
                # Close this window
                self.root.destroy()
                
                # Open verification window
                verify_root = tk.Toplevel()
                from verification import VerificationWindow
                VerificationWindow(verify_root, username, email, verification_code, 
                                 self.on_register_success, self.on_back_callback)
            else:
                messagebox.showerror("Error", "Failed to generate verification code")
        else:
            messagebox.showerror("Error", message)
    
    def on_register_success(self):
        """After successful registration and verification"""
        # Back to login
        self.on_back_callback()
    
    def back_to_login(self):
        """Go back to login"""
        self.root.destroy()
        self.on_back_callback()
