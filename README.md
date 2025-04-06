# Django CRUD Application

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

A complete Django web application demonstrating Create, Read, Update, and Delete (CRUD) operations with MySQL database integration.

## ✨ Features

- ✅ Full CRUD functionality for employee records
- ✅ MySQL database integration
- ✅ Model-Form-View architecture
- ✅ Bootstrap-styled templates
- ✅ Responsive design
- ✅ Form validation
- ✅ Pagination-ready structure

## 🚀 Quick Start

### Prerequisites
- Python 3.6+
- MySQL Server
- pip package manager

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/django-crud-app.git
   cd django-crud-app
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your MySQL database:
   ```sql
   CREATE DATABASE djangodb;
   ```

5. Configure database settings in `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'djangodb',
           'USER': 'your_username',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '3306'
       }
   }
   ```

6. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Start the development server:
   ```bash
   python manage.py runserver
   ```

8. Access the application at `http://localhost:8000/show`

## 📂 Project Structure

```
django-crud-app/
├── crudexample/            # Project configuration
├── employee/               # Employee app
│   ├── migrations/         # Database migrations
│   ├── static/             # Static files (CSS, JS, images)
│   ├── templates/          # HTML templates
│   │   ├── edit.html       # Edit employee form
│   │   ├── index.html      # Add employee form
│   │   └── show.html       # Employee listing
│   ├── admin.py            # Admin configuration
│   ├── apps.py             # App configuration
│   ├── forms.py            # Employee form
│   ├── models.py           # Employee model
│   ├── tests.py            # Test cases
│   └── views.py            # View functions
├── manage.py               # Django command-line utility
└── README.md               # This file
```

## 🖥️ Screenshots

| Add Employee | View Employees | Edit Employee |
|--------------|----------------|---------------|
| ![Add Employee](media/image10.png) | ![View Employees](media/image12.png) | ![Edit Employee](media/image13.png) |

## 🔧 Technologies Used

- **Backend**: Django 3.2+
- **Database**: MySQL
- **Frontend**: HTML5, Bootstrap
- **Templating**: Django Templates
- **Form Handling**: Django ModelForms

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📧 Contact

Your Name - prasadsapkal282@gmail.com

Project Link: [https://github.com/yourusername/django-crud-app](https://github.com/yourusername/django-crud-app)

---

Made with ❤️ and Django