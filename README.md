# Employee Form & Graphic Visualization

A Django web application for managing employee records with graphical data visualization.  
Assignment project for the **Web Interfaces & Services** course at **UPB-FIIR** (Universitatea Politehnica București – Facultatea de Inginerie în Limbi Străine).

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Database](#database)

---

## Overview

This application allows users to:

1. **Add employees** via an HTML form with client-side and server-side validation.
2. **View all employees** in a sortable, styled table.
3. **Delete employees** directly from the table.
4. **Visualize employee data** through auto-generated charts:
   - Pie chart showing gender distribution.
   - Bar chart showing job-category distribution.

---

## Features

| Feature | Description |
|---|---|
| Employee Form | Add employees with first name, last name, gender, and job category |
| Table View | Paginated table listing all employees stored in the database |
| Delete | Remove individual employee records from the table view |
| Graphs | Auto-generated pie and bar charts using Matplotlib |
| Navigation | Responsive Bootstrap 5 navbar with active-link highlighting |
| Validation | HTML5 + Bootstrap form validation with custom feedback messages |
| Admin Panel | Django admin interface with search, filter, and list display |

---

## Technology Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.x, Django 4.2.1 |
| Database | SQLite (default) / MySQL (optional) |
| Charts | Matplotlib 3.7, NumPy |
| Frontend | Bootstrap 5.2.3, jQuery 3.6 |
| Styling | Custom CSS (`custom.css`) |

---

## Project Structure

```
employeeForm_Graphic-project/
├── manage.py                        # Django management script
├── requirements.txt                 # Python dependencies
├── db.sqlite3                       # SQLite database (auto-created on first run)
│
├── employeeForm_Graphic/            # Django project configuration
│   ├── settings.py                  # Project settings (DB, static/media, apps)
│   ├── urls.py                      # Root URL configuration
│   ├── wsgi.py
│   └── asgi.py
│
└── formular/                        # Main Django application
    ├── models.py                    # Employee model definition
    ├── views.py                     # View functions (home, table, graphs, delete)
    ├── forms.py                     # EmployeeForm with custom widgets
    ├── admin.py                     # Admin panel registration
    ├── graph_utils.py               # Matplotlib chart generation logic
    │
    ├── migrations/                  # Database migrations
    │   ├── 0001_initial.py
    │   ├── 0002_project_delete_student.py
    │   └── 0003_employee_delete_project.py
    │
    ├── templates/formular/          # HTML templates
    │   ├── base.html                # Base layout (navbar, messages, scripts)
    │   ├── home.html                # Employee registration form
    │   ├── tableVisualization.html  # Employee table view
    │   └── showGraphs.html          # Graph display page
    │
    └── static/formular/             # Static assets
        ├── cs/
        │   └── custom.css           # Custom stylesheet
        ├── javascript/
        │   ├── navCollapse.js       # Navbar collapse animation (jQuery)
        │   └── navigation_highlight.js
        └── python/
            └── graphScripts.py      # (original location, kept for reference)
```

---

## Prerequisites

- **Python** 3.9 or newer
- **pip** (Python package manager)
- *(Optional)* A virtual environment tool such as `venv` or `conda`
- *(Optional, for MySQL backend)* MySQL Server 5.7+ and `mysqlclient` Python package

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/SkyDiVe3/employeeForm_Graphic-project.git
cd employeeForm_Graphic-project
```

### 2. Create and activate a virtual environment (recommended)

```bash
python -m venv venv

# On Linux / macOS
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

> **Note:** `mysqlclient` is **not** included in `requirements.txt` by default.  
> It is only needed when you configure a MySQL database (see [Configuration](#configuration)).  
> Install it separately with `pip install mysqlclient==2.1.1` if required.

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. (Optional) Create a Django superuser for the admin panel

```bash
python manage.py createsuperuser
```

---

## Configuration

All configurable settings live in `employeeForm_Graphic/settings.py`.  
Sensitive values can be overridden using **environment variables**.

| Environment Variable | Default | Description |
|---|---|---|
| `SECRET_KEY` | development key | Django secret key — **always** override in production |
| `DB_ENGINE` | `django.db.backends.sqlite3` | Database backend |
| `DB_NAME` | `employee_db` | Database name (MySQL only) |
| `DB_USER` | `root` | Database user (MySQL only) |
| `DB_PASSWORD` | *(empty)* | Database password (MySQL only) |
| `DB_HOST` | `127.0.0.1` | Database host (MySQL only) |
| `DB_PORT` | `3306` | Database port (MySQL only) |

### Switching to MySQL

1. Install the MySQL client library:
   ```bash
   pip install mysqlclient==2.1.1
   ```
2. Create a MySQL database and user.
3. Set the environment variables before starting the server:
   ```bash
   export DB_ENGINE=django.db.backends.mysql
   export DB_NAME=your_database
   export DB_USER=your_user
   export DB_PASSWORD=your_password
   ```
4. Re-run migrations: `python manage.py migrate`

---

## Running the Application

```bash
python manage.py runserver
```

Open your browser and navigate to **http://127.0.0.1:8000/**.

The Django admin panel is available at **http://127.0.0.1:8000/admin/**.

---

## Usage

### Pages & Routes

| URL | View | Description |
|---|---|---|
| `/` | `home` | Employee registration form |
| `/show/` | `showTableDB` | Table of all employees with delete buttons |
| `/graphs/` | `graphs` | Pie chart (gender) and bar chart (job category) |
| `/delete_employee/<id>/` | `delete_employee` | Deletes the specified employee (POST only) |
| `/admin/` | Django Admin | Full CRUD for employees |

### Adding an Employee

1. Open the home page (`/`).
2. Fill in **First Name**, **Last Name**, **Job Title**, and **Sex**.
3. Click **Inscrie angajat** (Register Employee).
4. A success message confirms the record was saved.

### Viewing Employees

Navigate to **See Employee** (`/show/`) in the navbar to see all employees in a table.  
Click **Delete** on any row to remove that employee.

### Viewing Charts

Navigate to **Graphs** (`/graphs/`) to generate and view:
- A **pie chart** showing the proportion of male / female / other employees.
- A **bar chart** showing how many employees belong to each job category.

Charts are generated on every page visit and saved to `media/formular/graphs/`.

---

## Database

### Employee Model

| Field | Type | Choices |
|---|---|---|
| `id` | BigAutoField (PK) | — |
| `first_name` | CharField(30) | — |
| `last_name` | CharField(30) | — |
| `gender` | CharField(6) | `other`, `male`, `female` |
| `job_category` | CharField(2) | `HR` (Human Resources), `SD` (Software Dev), `TE` (Tester) |
