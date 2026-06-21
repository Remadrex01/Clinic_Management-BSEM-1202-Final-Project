"""
Settings Module for Clinic Management System
"""

import tkinter as tk
from tkinter import ttk, messagebox


class SettingsWindow:
    """Settings window class"""
    
    def __init__(self, root, user_data):
        """Initialize settings window"""
        self.root = root
        self.user_data = user_data
        
        # Create window
        window = tk.Toplevel(root)
        window.title("Settings")
        window.geometry("600x500")
        window.resizable(False, False)
        
        # Center window
        self.center_window(window)
        
        # Setup styles
        self.setup_styles()
        
        # Create UI
        self.create_ui(window)
    
    def center_window(self, window):
        """Center window on screen"""
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry(f'{width}x{height}+{x}+{y}')
    
    def setup_styles(self):
        """Setup styles"""
        self.bg_color = "#F5F5F5"
        self.primary_color = "#5B9BD5"
        self.text_color = "#2C3E50"
        self.success_color = "#27AE60"
        self.warning_color = "#E74C3C"
    
    def create_ui(self, window):
        """Create settings UI"""
        window.configure(bg=self.bg_color)
        
        # Title
        title_frame = tk.Frame(window, bg=self.primary_color, height=60)
        title_frame.pack(fill=tk.X)
        title_frame.pack_propagate(False)
        
        title = tk.Label(title_frame, text="Settings", 
                        font=("Segoe UI", 16, "bold"), fg="white",
                        bg=self.primary_color)
        title.pack(pady=15)
        
        # Content frame
        content_frame = tk.Frame(window, bg="white")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Account info
        account_label = tk.Label(content_frame, text="Account Information", 
                                font=("Segoe UI", 12, "bold"), fg=self.text_color,
                                bg="white")
        account_label.pack(anchor=tk.W, pady=(0, 15))
        
        # User info frame
        info_frame = tk.Frame(content_frame, bg="#F9F9F9", relief=tk.FLAT, bd=1)
        info_frame.pack(fill=tk.X, pady=(0, 20))
        
        tk.Label(info_frame, text=f"Full Name: {self.user_data['full_name']}", 
                font=("Segoe UI", 10), fg=self.text_color, bg="#F9F9F9").pack(anchor=tk.W, padx=15, pady=10)
        
        tk.Label(info_frame, text=f"Username: {self.user_data['username']}", 
                font=("Segoe UI", 10), fg=self.text_color, bg="#F9F9F9").pack(anchor=tk.W, padx=15, pady=5)
        
        tk.Label(info_frame, text=f"Email: {self.user_data['email']}", 
                font=("Segoe UI", 10), fg=self.text_color, bg="#F9F9F9").pack(anchor=tk.W, padx=15, pady=5)
        
        if self.user_data.get('phone'):
            tk.Label(info_frame, text=f"Phone: {self.user_data['phone']}", 
                    font=("Segoe UI", 10), fg=self.text_color, bg="#F9F9F9").pack(anchor=tk.W, padx=15, pady=5)
        
        tk.Label(info_frame, text=f"Role: {self.user_data.get('role', 'User')}", 
                font=("Segoe UI", 10), fg=self.text_color, bg="#F9F9F9").pack(anchor=tk.W, padx=15, pady=(5, 10))
        
        # Preferences section
        pref_label = tk.Label(content_frame, text="Preferences", 
                             font=("Segoe UI", 12, "bold"), fg=self.text_color,
                             bg="white")
        pref_label.pack(anchor=tk.W, pady=(20, 15))
        
        # Theme preference
        theme_frame = tk.Frame(content_frame, bg="white")
        theme_frame.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(theme_frame, text="Color Theme:", 
                font=("Segoe UI", 10), fg=self.text_color, bg="white").pack(anchor=tk.W, pady=(0, 5))
        
        theme_var = tk.StringVar(value="Light")
        theme_combo = ttk.Combobox(theme_frame, textvariable=theme_var,
                                  values=["Light", "Dark"], state="readonly",
                                  font=("Segoe UI", 9), width=30)
        theme_combo.pack(fill=tk.X)
        
        # Font size preference
        font_frame = tk.Frame(content_frame, bg="white")
        font_frame.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(font_frame, text="Font Size:", 
                font=("Segoe UI", 10), fg=self.text_color, bg="white").pack(anchor=tk.W, pady=(0, 5))
        
        font_var = tk.StringVar(value="Normal")
        font_combo = ttk.Combobox(font_frame, textvariable=font_var,
                                 values=["Small", "Normal", "Large"],
                                 state="readonly",
                                 font=("Segoe UI", 9), width=30)
        font_combo.pack(fill=tk.X)
        
        # Language preference
        lang_frame = tk.Frame(content_frame, bg="white")
        lang_frame.pack(fill=tk.X, pady=(0, 20))
        
        tk.Label(lang_frame, text="Language:", 
                font=("Segoe UI", 10), fg=self.text_color, bg="white").pack(anchor=tk.W, pady=(0, 5))
        
        lang_var = tk.StringVar(value="English")
        lang_combo = ttk.Combobox(lang_frame, textvariable=lang_var,
                                 values=["English"], state="readonly",
                                 font=("Segoe UI", 9), width=30)
        lang_combo.pack(fill=tk.X)
        
        # System info
        info_label = tk.Label(content_frame, text="System Information", 
                             font=("Segoe UI", 12, "bold"), fg=self.text_color,
                             bg="white")
        info_label.pack(anchor=tk.W, pady=(20, 15))
        
        # System info frame
        sys_frame = tk.Frame(content_frame, bg="#F9F9F9", relief=tk.FLAT, bd=1)
        sys_frame.pack(fill=tk.X, pady=(0, 20))
        
        tk.Label(sys_frame, text="Application: Clinic Management System v1.0", 
                font=("Segoe UI", 9), fg=self.text_color, bg="#F9F9F9").pack(anchor=tk.W, padx=15, pady=10)
        
        tk.Label(sys_frame, text="Database: SQLite 3", 
                font=("Segoe UI", 9), fg=self.text_color, bg="#F9F9F9").pack(anchor=tk.W, padx=15, pady=5)
        
        tk.Label(sys_frame, text="Framework: Python Tkinter", 
                font=("Segoe UI", 9), fg=self.text_color, bg="#F9F9F9").pack(anchor=tk.W, padx=15, pady=(5, 10))
        
        # Buttons frame
        buttons_frame = tk.Frame(content_frame, bg="white")
        buttons_frame.pack(fill=tk.X, pady=(20, 0))
        
        save_btn = tk.Button(buttons_frame, text="Save", 
                           font=("Segoe UI", 10, "bold"),
                           bg=self.success_color, fg="white",
                           cursor="hand2", command=lambda: self.save_settings(window, theme_var, font_var, lang_var),
                           padx=15, pady=8, relief=tk.FLAT, bd=0)
        save_btn.pack(side=tk.LEFT, padx=5)
        
        close_btn = tk.Button(buttons_frame, text="Close", 
                            font=("Segoe UI", 10, "bold"),
                            bg=self.text_color, fg="white",
                            cursor="hand2", command=window.destroy,
                            padx=15, pady=8, relief=tk.FLAT, bd=0)
        close_btn.pack(side=tk.LEFT, padx=5)
    
    def save_settings(self, window, theme_var, font_var, lang_var):
        """Save settings"""
        messagebox.showinfo("Success", 
                          f"Settings saved successfully!\n\n"
                          f"Theme: {theme_var.get()}\n"
                          f"Font Size: {font_var.get()}\n"
                          f"Language: {lang_var.get()}")
