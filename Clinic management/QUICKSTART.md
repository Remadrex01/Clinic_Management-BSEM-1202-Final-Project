# Clinic Management System - Quick Start Guide

## Get Started in 3 Steps

### Step 1: Verify Python Installation
Open command prompt and run:
```bash
python --version
```
Ensure you have Python 3.7 or higher installed.

### Step 2: Verify Tkinter
Run:
```bash
python -m tkinter
```
A small window should appear. If it does, tkinter is installed.

### Step 3: Run the Application
Navigate to the project folder and run:
```bash
python main.py
```

The application should launch with the login screen.

---

## First User Setup

### Create Your Account (First Time Only)

1. Click **"Register Here"** on the login screen
2. Fill in the registration form:
   - **Full Name**: Your name
   - **Username**: Choose a username (must be unique)
   - **Email**: Your email address
   - **Phone**: Your phone number
   - **Password**: Create a strong password (min 6 characters)
3. Click **"Register"**
4. You'll be taken back to login screen

### Login
1. Enter your **Username** and **Password**
2. Click **"Login"**
3. Welcome to the dashboard!

---

## Dashboard Overview

Once logged in, you'll see:

### Left Sidebar Navigation
- 📊 **Dashboard** - View statistics and recent appointments
- 👥 **Patients** - Manage patient records
- 👨‍⚕️ **Doctors** - Manage doctor information
- 📅 **Appointments** - Schedule appointments
- 💊 **Pharmacy** - Manage medicine inventory
- 💰 **Billing** - Create and track bills
- 📈 **Reports** - View reports and analytics
- ⚙️ **Settings** - Manage preferences
- 🚪 **Logout** - Exit application

### Dashboard Cards
- **Total Patients**: Number of registered patients
- **Total Doctors**: Number of registered doctors
- **Total Appointments**: All scheduled appointments
- **Total Revenue**: Total billing amount

---

## Common Tasks

### Adding a Patient
1. Click **"Patients"** in sidebar
2. Click **"Add Patient"** button
3. Fill in patient details:
   - Full Name
   - Age
   - Gender
   - Phone Number
   - Address
   - Email (optional)
   - Blood Group (optional)
   - Medical History (optional)
4. Click **"Save"**

### Booking an Appointment
1. Click **"Appointments"** in sidebar
2. Click **"Book Appointment"** button
3. Select:
   - Patient from dropdown
   - Doctor from dropdown
   - Appointment date (YYYY-MM-DD format)
   - Appointment time (HH:MM format)
   - Status
   - Notes (optional)
4. Click **"Book"**

### Creating a Bill
1. Click **"Billing"** in sidebar
2. Click **"Create Bill"** button
3. Fill in:
   - Select Patient
   - Amount (in ₹)
   - Payment Method (Cash, Card, etc.)
   - Bill Date
   - Status
   - Notes (optional)
4. Click **"Create"**

### Viewing Reports
1. Click **"Reports"** in sidebar
2. Choose a report type:
   - Patient Report
   - Doctor Report
   - Appointment Report
   - Revenue Report

---

## Searching Records

Most modules have a search feature:
1. Enter search term in the search box
2. Results update in real-time
3. Leave empty to view all records

---

## Tips

✅ **Search is your friend** - Use it to quickly find records
✅ **Double-click rows** - Edit patient/doctor/medicine details
✅ **Check date format** - Use YYYY-MM-DD (e.g., 2024-01-15)
✅ **Check time format** - Use HH:MM in 24-hour format (e.g., 14:30)
✅ **Backup data** - Copy database/clinic.db regularly

---

## Need Help?

### Application won't start?
- Make sure you're in the correct folder
- Run: `python main.py`
- Ensure Python 3.7+ is installed

### Can't create account?
- Username must be unique
- Email must be unique
- Password must be at least 6 characters

### Data not saving?
- Ensure `database/` folder exists
- Check disk space available
- Restart the application

### Forgot password?
- Currently, you need to create a new account
- Use a different username

---

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| Enter | Submit form |
| Tab | Move to next field |
| Double-click | Edit record |

---

## File Locations

After running the application:
- **Database file**: `database/clinic.db`
- **Backup**: Copy `database/clinic.db` to backup location
- **Restore**: Copy backup file back to `database/clinic.db`

---

## System Requirements

- **OS**: Windows, macOS, Linux
- **Python**: 3.7 or higher
- **RAM**: 512MB minimum
- **Storage**: 50MB minimum
- **Screen**: 1024x768 minimum resolution

---

## Next Steps

1. ✅ Create your account
2. ✅ Add some doctors
3. ✅ Add some patients
4. ✅ Schedule appointments
5. ✅ Create bills
6. ✅ View reports

**Happy clinic managing!** 🏥

---

For detailed documentation, see **README.md**
