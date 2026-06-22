# Clinic Management System

A comprehensive, professional, and open-source Clinic Management System built with Python Tkinter and SQLite. Designed to democratize healthcare management for clinics, hospitals, and medical centers globally.

<div align="center">

### 🌍 Advancing Global Health through Technology
**Aligned with UN Sustainable Development Goal 3: Good Health and Well-being**

</div>

---

## 🎯 Project Mission

This project aims to make clinic management accessible to healthcare providers worldwide, particularly in resource-limited settings. By providing a free, open-source solution, we help healthcare facilities:
- **Improve efficiency** in patient care management
- **Reduce administrative burden** on healthcare staff
- **Enable better patient outcomes** through organized data management
- **Support healthcare accessibility** in underserved communities

---

## 🌱 Sustainable Development Goal (SDG) Alignment

### **SDG 3: Good Health and Well-being**

#### How We Help Achieve This Goal:

| SDG Target | How Clinic Management System Helps |
|-----------|-------------------------------------|
| **3.1** - Reduce maternal mortality | Organized appointment scheduling and patient tracking improve continuity of care |
| **3.3** - Combat communicable diseases | Patient medical history tracking enables better disease monitoring |
| **3.8** - Achieve universal health coverage | Affordable, accessible clinic management supports healthcare service delivery |
| **3.9** - Reduce deaths from pollution | Streamlined operations reduce paper waste and environmental impact |

#### Impact for Collaborators:

By contributing to this project, you:
- 🏥 **Help healthcare providers** manage 1000s of patients more efficiently
- 💡 **Enable innovation** in healthcare delivery globally
- 🌍 **Support underserved communities** with free, sustainable technology
- 📊 **Build your portfolio** while solving real-world healthcare challenges
- 🤝 **Join a community** dedicated to global health equity

---

## ✨ Features

### 🔐 User Authentication
- Secure login system with SHA-256 password hashing
- User registration with validation
- Role-based access control (extensible)
- Secure session management

### 👥 Patient Management
- Add, edit, delete, and search patients
- Comprehensive patient profiles (demographics, contact, blood type, medical history)
- Advanced search and filtering capabilities
- Patient list sorting

### 👨‍⚕️ Doctor Management
- Doctor profiles with specialization and qualifications
- Experience tracking
- Contact information management
- Doctor availability management

### 📅 Appointment Management
- Book, edit, and cancel appointments
- Schedule coordination between patients and doctors
- Appointment status tracking (scheduled, completed, cancelled)
- Appointment notes for clinical context

### 💊 Pharmacy Module
- Medicine inventory management
- Add, edit, and delete medicine records
- Expiry date tracking
- Price and manufacturer information
- Quantity monitoring

### 💰 Billing Module
- Bill creation and management
- Multiple payment method support (Cash, Card, UPI, Cheque)
- Payment status tracking
- Bill notes for record-keeping

### 📊 Reports & Analytics
- Patient reports with complete details
- Doctor performance reports
- Appointment statistics and history
- Revenue and financial analytics
- Dashboard metrics for quick insights

### 📈 Dashboard
- Key performance indicators (KPIs):
  - Total patients
  - Total doctors
  - Total appointments
  - Total revenue
- Recent appointments overview
- Quick navigation to all modules

### ⚙️ Settings
- User account management
- Application preferences
- System information display
- Theme and font customization

---

## 🏗️ Project Architecture

```
clinic-management/
│
├── main.py                 # Application entry point
├── database.py             # Database operations and schema
├── login.py                # Authentication interface
├── register.py             # User registration interface
├── dashboard.py            # Main dashboard with navigation
├── patients.py             # Patient management module
├── doctors.py              # Doctor management module
├── appointments.py         # Appointment scheduling module
├── pharmacy.py             # Pharmacy inventory module
├── billing.py              # Billing and invoicing module
├── reports.py              # Reports and analytics module
├── settings.py             # Settings and preferences module
│
├── assets/
│ ├── icons/               # Application icons
│ └── images/              # Application images
│
├── database/
│ └── clinic.db            # SQLite database (auto-created)
│
└── docs/
    ├── ARCHITECTURE.md    # Technical architecture details
    ├── CONTRIBUTING.md    # Contribution guidelines
    ├── DEVELOPMENT.md     # Developer setup guide
    ├── CODE_OF_CONDUCT.md # Community guidelines
    └── API.md             # Module API documentation
```

---

## 🚀 Quick Start

### Prerequisites
- **Python 3.7+** (or higher)
- **Tkinter** (included with Python)
- **SQLite3** (included with Python)
- No external package installations required!

### Installation (3 Steps)

#### Step 1: Clone or Download the Repository
```bash
git clone https://github.com/yourusername/clinic-management.git
cd clinic-management
```

#### Step 2: Verify Your Environment
```bash
# Verify Python version
python --version  # Should be 3.7 or higher

# Verify Tkinter
python -m tkinter  # A small window should appear
```

#### Step 3: Run the Application
```bash
python main.py
```

The login screen will appear. First-time users should click **"Register Here"** to create an account.

---

## 📖 Documentation

We provide comprehensive documentation for users and developers:

| Document | Purpose |
|----------|---------|
| [QUICKSTART.md](QUICKSTART.md) | Get up and running in 5 minutes |
| [SETUP_GUIDE.md](SETUP_GUIDE.md) | Detailed installation and configuration |
| [ARCHITECTURE.md](docs/ARCHITECTURE.md) | Technical architecture and design patterns |
| [DEVELOPMENT.md](docs/DEVELOPMENT.md) | Developer setup and contribution workflow |
| [CONTRIBUTING.md](docs/CONTRIBUTING.md) | How to contribute to the project |
| [CODE_OF_CONDUCT.md](docs/CODE_OF_CONDUCT.md) | Community guidelines and conduct expectations |

---

## 🤝 Contributing

We warmly welcome contributions from developers, healthcare professionals, and enthusiasts worldwide!

### Ways You Can Contribute

#### 💻 **Code Contributions**
- Bug fixes and improvements
- New features for clinic management
- Performance optimization
- Code quality enhancements

#### 📝 **Documentation**
- Improve existing documentation
- Add multilingual support to docs
- Create video tutorials
- Write case studies

#### 🌍 **Localization**
- Translate UI to new languages
- Adapt documentation for different regions
- Cultural customization

#### 🧪 **Testing**
- Test the system in various environments
- Report bugs and issues
- Suggest improvements

#### 📢 **Community**
- Help other users
- Share your use cases
- Promote the project in your network

### Getting Started as a Contributor

1. **Read** [CONTRIBUTING.md](docs/CONTRIBUTING.md) for detailed guidelines
2. **Follow** [DEVELOPMENT.md](docs/DEVELOPMENT.md) to set up your development environment
3. **Review** [CODE_OF_CONDUCT.md](docs/CODE_OF_CONDUCT.md) to understand our community values
4. **Fork** the repository and start contributing!

---

## 📋 Technology Stack

| Component | Technology |
|-----------|-----------|
| **Frontend** | Python Tkinter |
| **Backend** | Python (OOP) |
| **Database** | SQLite 3 |
| **Architecture** | MVC (Model-View-Controller) |
| **Design Pattern** | Object-Oriented Programming |

**Why These Technologies?**
- ✅ **No external dependencies** - works on any system with Python
- ✅ **Lightweight** - suitable for low-resource environments
- ✅ **Cross-platform** - runs on Windows, Linux, macOS
- ✅ **Easy to maintain** - simple, readable code structure
- ✅ **Educational** - great for learning Python and GUI development

---

## 📊 Current Statistics

- **Modules**: 11 core modules
- **Database Tables**: 6 (Users, Patients, Doctors, Appointments, Medicines, Bills)
- **Lines of Code**: ~3000+
- **Languages**: Python
- **Setup Time**: < 2 minutes

---

## 🐛 Reporting Issues

Found a bug or have a feature request? Please:

1. Check [existing issues](issues) to avoid duplicates
2. Create a new issue with:
   - Clear title and description
   - Steps to reproduce (for bugs)
   - Expected vs. actual behavior
   - Screenshots (if applicable)
   - Your environment (Python version, OS)

---

## 💬 Getting Help

- 📖 **Documentation**: Check the docs folder
- 💡 **Questions**: Open a Discussion
- 🐛 **Bugs**: Report via Issues
- 💬 **Chat**: Join our community discussions

---

## 📄 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

This means:
- ✅ Free for commercial use
- ✅ Free for personal use
- ✅ You can modify the code
- ✅ You can distribute it
- ⚠️ Include license and copyright notice

---

## 🌟 Recognition

### Our Contributors
We recognize and celebrate all contributors who help make this project better. Every contribution, big or small, matters!

### Citation
If you use this project in your research or work, please cite:

```bibtex
@software{clinic_management_2024,
  author = {Your Name},
  title = {Clinic Management System - Open Source Healthcare Solution},
  year = {2024},
  url = {https://github.com/yourusername/clinic-management}
}
```

---

## 🔮 Roadmap

### Version 1.1 (Q3 2024)
- [ ] User role-based permissions
- [ ] Medicine prescription management
- [ ] Patient reminder system
- [ ] Multi-language UI support

### Version 2.0 (Q4 2024)
- [ ] Web-based dashboard
- [ ] Mobile app version
- [ ] API for third-party integrations
- [ ] Advanced reporting and BI features

### Vision
Make clinic management accessible to **1 million healthcare providers** globally by 2025.

---

## 📞 Contact & Support

- **Email**: clinic-management@example.com
- **GitHub**: [Project Repository](https://github.com/yourusername/clinic-management)
- **Issues**: [Bug Reports & Features](issues)
- **Discussions**: [Community Forum](discussions)

---

## 🙏 Acknowledgments

- Built with ❤️ for global healthcare
- Inspired by the UN Sustainable Development Goals
- Special thanks to all contributors and users

---

<div align="center">

**Made with ❤️ to improve healthcare delivery worldwide**

[⭐ Star us on GitHub](https://github.com/yourusername/clinic-management) | [🐛 Report an Issue](issues) | [📖 Read the Docs](docs/)

</div>
```bash
python main.py
```

The application will:
1. Create the database folder if it doesn't exist
2. Initialize all required tables in the SQLite database
3. Launch the login window

## Usage Guide

### First Time Setup

1. **Register an Account**
   - Click "Register Here" on the login page
   - Fill in your details:
     - Full Name
     - Username (unique)
     - Email (unique)
     - Phone Number
     - Password (minimum 6 characters)
   - Click "Register" button
   - You'll be redirected to login page

2. **Login**
   - Enter your username and password
   - Optional: Check "Remember Me" to auto-fill credentials next time
   - Optional: Check "Show Password" to see your password
   - Click "Login" button

### After Login

#### Dashboard
- View key statistics (patients, doctors, appointments, revenue)
- See recent appointments
- Access all modules from the sidebar

#### Patient Management
- **Add Patient**: Click "Add Patient" to register a new patient
- **View Patients**: All registered patients are shown in the table
- **Search**: Use the search box to find patients by name, phone, or ID
- **Edit Patient**: Double-click a patient or click "Edit Patient"
- **Delete Patient**: Select a patient and click "Delete Patient"

#### Doctor Management
- **Add Doctor**: Register a new doctor with specialization
- **View Doctors**: List of all doctors with their specializations
- **Search**: Find doctors by name or specialization
- **Edit Doctor**: Modify doctor information
- **Delete Doctor**: Remove doctor from system

#### Appointment Management
- **Book Appointment**: Schedule new appointments with date, time, and notes
- **View Appointments**: See all scheduled appointments
- **Edit Appointment**: Change appointment details or status
- **Cancel Appointment**: Remove or cancel appointments

#### Pharmacy Module
- **Add Medicine**: Add new medicines to inventory
- **Track Inventory**: Monitor quantity and expiry dates
- **Edit Medicine**: Update medicine information
- **Delete Medicine**: Remove expired or discontinued medicines

#### Billing Module
- **Create Bill**: Generate new bills for patients
- **Payment Tracking**: Track payment methods and status
- **Edit Bill**: Modify bill details
- **Delete Bill**: Remove bills if needed

#### Reports
- **Patient Report**: Complete patient database export
- **Doctor Report**: Doctor information and statistics
- **Appointment Report**: Full appointment history
- **Revenue Report**: Financial analytics and billing summary

#### Settings
- View your account information
- Customize application preferences
- View system information

### Sidebar Navigation
- 📊 Dashboard - Main dashboard
- 👥 Patients - Patient management
- 👨‍⚕️ Doctors - Doctor management
- 📅 Appointments - Appointment scheduling
- 💊 Pharmacy - Medicine inventory
- 💰 Billing - Patient billing
- 📈 Reports - Analytics and reports
- ⚙️ Settings - Preferences
- 🚪 Logout - Exit application

## Database Schema

### Users Table
- user_id (Primary Key)
- username (Unique)
- password (Hashed)
- full_name
- email (Unique)
- phone
- role
- created_at

### Patients Table
- patient_id (Primary Key)
- full_name
- age
- gender
- phone
- address
- email
- blood_group
- medical_history
- created_at
- updated_at

### Doctors Table
- doctor_id (Primary Key)
- name
- specialization
- phone
- email
- qualification
- experience_years
- available_days
- created_at
- updated_at

### Appointments Table
- appointment_id (Primary Key)
- patient_id (Foreign Key)
- doctor_id (Foreign Key)
- appointment_date
- appointment_time
- status
- notes
- created_at

### Medicines Table
- medicine_id (Primary Key)
- medicine_name
- quantity
- price
- expiry_date
- manufacturer
- description
- created_at
- updated_at

### Billing Table
- bill_id (Primary Key)
- patient_id (Foreign Key)
- amount
- payment_method
- status
- bill_date
- notes
- created_at

## Security Features

1. **Password Security**
   - Passwords are hashed using SHA-256
   - Never stored in plain text
   - Verified during login

2. **Data Validation**
   - Input validation for all forms
   - Error handling and user feedback
   - Database constraints and relationships

3. **User Session**
   - Secure user authentication
   - Session management
   - Logout functionality

## System Requirements

- **OS**: Windows, macOS, or Linux
- **RAM**: Minimum 512MB
- **Storage**: Minimum 50MB for application and database
- **Display**: 1024x768 minimum resolution

## Keyboard Shortcuts

- `Enter` - Submit form or button click
- `Tab` - Navigate between fields
- Double-click - Edit patient/doctor/medicine

## Tips & Best Practices

1. **Regular Backups**: Backup the `database/clinic.db` file regularly
2. **Data Entry**: Always verify information before saving
3. **Search**: Use search functionality to quickly find records
4. **Reports**: Generate reports regularly for business insights
5. **Password**: Keep your login credentials secure

## Troubleshooting

### Application Won't Start
- Ensure Python 3.7+ is installed
- Check if all Python files are in the correct directory
- Try running: `python main.py` from command prompt

### Database Errors
- Ensure `database/` folder exists
- Check disk space is available
- Try deleting `database/clinic.db` to reset (WARNING: This deletes all data)

### GUI Display Issues
- Increase screen resolution to minimum 1024x768
- Ensure Python Tkinter is installed

## Features for School Projects

This system is ideal for:
- ✅ School database projects
- ✅ Python learning and practice
- ✅ GUI application development
- ✅ Database design and management
- ✅ Software engineering concepts
- ✅ Complete working application example

## Code Quality

- **Object-Oriented Design**: Clean OOP structure
- **Modularity**: Separate modules for each feature
- **Error Handling**: Comprehensive exception handling
- **Documentation**: Well-commented code
- **Best Practices**: Follows Python conventions

## License

This project is open source and available for educational and personal use.

## Support & Contribution

For issues, suggestions, or improvements:
- Review the code and documentation
- Ensure all requirements are met
- Test thoroughly before deployment

## Version History

- **v1.0** - Initial release with all features
  - User authentication system
  - Patient management
  - Doctor management
  - Appointment scheduling
  - Pharmacy inventory
  - Billing system
  - Reports and analytics
  - Dashboard

---

**Developed as a complete clinic management solution using Python Tkinter and SQLite**

For more information, refer to the individual module documentation in each Python file.
