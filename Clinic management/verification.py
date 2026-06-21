"""
Email Verification Module for Clinic Management System
Handles email verification process after registration
"""

import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tkFont
from database import DatabaseManager


class VerificationWindow:
    """Email verification window class"""
    
    def __init__(self, root, username, email, verification_code, on_success_callback, on_back_callback):
        """Initialize verification window"""
        self.root = root
        self.username = username
        self.email = email
        self.verification_code = verification_code
        self.on_success_callback = on_success_callback
        self.on_back_callback = on_back_callback
        self.db = DatabaseManager()
        
        # Configure window
        self.root.title("Clinic Management System - Email Verification")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Center window on screen
        self.center_window()
        
        # Configure style
        self.setup_styles()
        
        # Create UI
        self.create_verification_ui()
    
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
        self.success_color = "#27AE60"
        self.warning_color = "#E74C3C"
        
        self.root.configure(bg=self.bg_color)
    
    def create_verification_ui(self):
        """Create verification UI"""
        # Main container
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Center container for card
        center_frame = tk.Frame(main_frame, bg=self.bg_color)
        center_frame.pack(expand=True)
        
        # Verification card
        card_frame = tk.Frame(center_frame, bg=self.bg_color, relief=tk.FLAT, bd=0)
        card_frame.pack()
        
        # Shadow effect
        shadow = tk.Frame(card_frame, bg=self.border_color)
        shadow.pack(padx=2, pady=2, fill=tk.BOTH)
        
        # Main card content
        verify_card = tk.Frame(shadow, bg=self.bg_color)
        verify_card.pack(padx=2, pady=2, fill=tk.BOTH, expand=True)
        
        # Header section
        header_frame = tk.Frame(verify_card, bg=self.primary_color)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Title
        title = tk.Label(header_frame, text="📧 Verify Your Email", 
                        font=("Segoe UI", 20, "bold"), 
                        fg="white", bg=self.primary_color)
        title.pack(pady=15)
        
        # Content frame
        content_frame = tk.Frame(verify_card, bg=self.bg_color)
        content_frame.pack(padx=40, pady=20, fill=tk.BOTH, expand=True)
        
        # Info message
        info_text = f"We've sent a verification code to:\n{self.email}"
        info_label = tk.Label(content_frame, text=info_text, 
                            font=("Segoe UI", 10), 
                            fg=self.text_color, bg=self.bg_color,
                            justify=tk.CENTER)
        info_label.pack(pady=(0, 30))
        
        # Code display section (for testing - in production this would be just the input)
        code_display_frame = tk.Frame(content_frame, bg=self.secondary_color, relief=tk.FLAT, bd=1)
        code_display_frame.pack(fill=tk.X, pady=(0, 20))
        
        test_label = tk.Label(code_display_frame, 
                            text="[Testing Mode] Your Verification Code:", 
                            font=("Segoe UI", 9, "bold"), 
                            fg=self.text_color, bg=self.secondary_color)
        test_label.pack(pady=(10, 5), padx=10)
        
        code_display = tk.Label(code_display_frame, text=self.verification_code, 
                              font=("Segoe UI", 24, "bold"), 
                              fg=self.primary_color, bg=self.secondary_color)
        code_display.pack(pady=(5, 10))
        
        note_label = tk.Label(code_display_frame, 
                             text="Replace with SMTP email sender in production. This code expires in 15 minutes.", 
                             font=("Segoe UI", 8), 
                             fg="#666666", bg=self.secondary_color)
        note_label.pack(pady=(0, 10), padx=10)
        
        # Enter code section
        code_label = tk.Label(content_frame, text="Enter Verification Code", 
                            font=("Segoe UI", 10, "bold"), 
                            fg=self.text_color, bg=self.bg_color)
        code_label.pack(anchor=tk.W, pady=(0, 10))
        
        self.code_var = tk.StringVar()
        code_entry = ttk.Entry(content_frame, textvariable=self.code_var, 
                              width=35, font=("Segoe UI", 12),
                              justify=tk.CENTER)
        code_entry.pack(fill=tk.X, pady=(0, 30))
        code_entry.focus()
        
        # Button frame
        button_frame = tk.Frame(content_frame, bg=self.bg_color)
        button_frame.pack(fill=tk.X, pady=(10, 0))
        
        # Verify button
        verify_btn = tk.Button(button_frame, text="✓ Verify Code", 
                             font=("Segoe UI", 10, "bold"),
                             bg=self.success_color, fg="white",
                             cursor="hand2", command=self.verify_code,
                             padx=20, pady=8, relief=tk.FLAT, bd=0)
        verify_btn.pack(side=tk.LEFT, padx=(0, 10), fill=tk.X, expand=True)
        
        # Back button
        back_btn = tk.Button(button_frame, text="← Back", 
                           font=("Segoe UI", 10, "bold"),
                           bg=self.secondary_color, fg=self.text_color,
                           cursor="hand2", command=self.go_back,
                           padx=20, pady=8, relief=tk.FLAT, bd=0)
        back_btn.pack(side=tk.LEFT, fill=tk.X, expand=True)
    
    def verify_code(self):
        """Verify the entered code"""
        entered_code = self.code_var.get().strip()
        
        if not entered_code:
            messagebox.showerror("Error", "Please enter the verification code")
            return
        
        if entered_code != self.verification_code:
            messagebox.showerror("Error", "Invalid verification code. Please try again.")
            self.code_var.set("")
            return
        
        # Verify email in database
        success, message = self.db.verify_email(self.username, self.verification_code)
        
        if success:
            messagebox.showinfo("Success", 
                              "Email verified successfully!\n\nYou can now login with your credentials.")
            self.root.destroy()
            self.on_success_callback()
        else:
            messagebox.showerror("Error", message)
    
    def go_back(self):
        """Go back to login"""
        if messagebox.askyesno("Confirm", "Go back to login without verifying?"):
            self.root.destroy()
            self.on_back_callback()
