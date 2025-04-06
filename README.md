# Employee Management System 🏢

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![GitHub last commit](https://img.shields.io/github/last-commit/prasadsapkal55/Employee-Management-?color=blue)

A lightweight Django-based Employee Management System with full CRUD functionality developed by Prasad Sapkal.

## ✨ Features

- **Simple Employee Management**:
  - Add, view, edit, and delete employee records
  - SQLite database (no additional setup required)
  - Clean Bootstrap interface
- **Easy to Deploy**:
  - Default Django SQLite configuration
  - Minimal dependencies
  - Ready-to-run structure

## 🚀 Getting Started

### Installation 

```bash
# 1. Clone the repository
git clone https://github.com/prasadsapkal55/Employee-Management-.git
cd Employee-Management-

# 2. Set up virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create superuser (optional for admin access):
python manage.py createsuperuser

# 5. Setup database
python manage.py makemigrations  # Create migrations from models
python manage.py migrate        # Apply migrations to database

# 6. Run the development server:
python manage.py runserver

# 7. Access the application at:
   - Main interface: `http://localhost:8000/show`
   - Admin panel: `http://localhost:8000/admin` (if superuser created)
```
## 📂 Project Structure

```
Employee-Management-/
├── employee/                  # Main application
│   ├── migrations/            # Database migrations
│   ├── static/                # Static files (CSS, JS)
│   ├── templates/             # HTML templates
│   │   ├── edit.html          # Edit employee
│   │   ├── index.html         # Add employee
│   │   └── show.html          # Show all employees
│   ├── admin.py               # Admin configuration
│   ├── apps.py                # App config
│   ├── forms.py               # Employee forms
│   ├── models.py              # Data models
│   ├── tests.py               # Tests
│   └── views.py               # View functions
├── EmployeeManagement/         # Project config
├── manage.py                   # Django CLI
└── README.md                   # This file
```

## 🖼️ Screenshots

| Feature | Screenshot |
|---------|------------|
| **Add Employee** | ![Add Employee](https://github.com/prasadsapkal55/Employee-Management-/blob/main/screenshots/add_employee.png) |
| **View Employees** | ![View Employees](https://github.com/prasadsapkal55/Employee-Management-/blob/main/screenshots/view_employees.png) |
| **Edit Employee** | ![Edit Employee](https://github.com/prasadsapkal55/Employee-Management-/blob/main/screenshots/edit_employee.png) |

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -m 'Add some NewFeature'`)
4. Push to the branch (`git push origin feature/NewFeature`)
5. Open a Pull Request


## 📧 Contact

Prasad Sapkal  
Email: [prasadsapkal282@gmail.com](mailto:prasadsapkal282@gmail.com)  
GitHub: [@prasadsapkal55](https://github.com/prasadsapkal55)

---

⭐ Feel free to star the repository if you find this project useful!
