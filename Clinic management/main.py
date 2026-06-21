"""
Clinic Management System - Main Entry Point
Clean separation between authentication flow and dashboard
"""

import tkinter as tk
from tkinter import messagebox
from database import DatabaseManager
from login import LoginWindow
from dashboard import Dashboard


class ClinicManagementApp:
    """Main application class"""
    
    def __init__(self):
        """Initialize the application"""
        # Create root window
        self.root = tk.Tk()
        
        # Initialize database
        try:
            self.db = DatabaseManager()
        except Exception as e:
            messagebox.showerror("Database Error", f"Could not initialize database: {str(e)}")
            self.root.destroy()
            return
        
        # Start with login window
        self.show_login()
    
    def show_login(self):
        """Show login window"""
        LoginWindow(self.root, self.on_login_success)
    
    def on_login_success(self, user_data):
        """Handle successful login - open dashboard in new window"""
        # Destroy the login window completely
        self.root.destroy()
        
        # Create a new window for the dashboard
        dashboard_root = tk.Tk()
        Dashboard(dashboard_root, user_data)
        
        # Run the dashboard window
        dashboard_root.mainloop()
    
    def run(self):
        """Run the application"""
        self.root.mainloop()


def main():
    """Main function"""
    app = ClinicManagementApp()
    app.run()


if __name__ == "__main__":
    main()
