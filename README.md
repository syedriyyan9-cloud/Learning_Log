📘 Learning Log – Django Web Application

A web-based learning journal built using Django 5.1 and Python 3.12.8.
This application allows users to create topics and log entries under each topic while maintaining secure user-specific data access.

This project was built as part of my backend learning journey and focuses on understanding Django’s core systems including authentication, models, views, templates, and CRUD operations.

🚀 Live Demo

Deployed on Render:
🔗 (https://learning-log-lcr9.onrender.com)

📌 Features

User registration and authentication (Django built-in auth system)

Create, read, update topics

Create, read, update entries under topics

User-specific data isolation (each user sees only their data)

Bootstrap-based responsive UI

SQLite database integration

Secure login/logout system

CSRF protection enabled

🏗️ Technical Concepts Implemented

This project demonstrates understanding of:

Django MVT (Model-View-Template) architecture

Django ORM for database operations

One-to-Many relationships (Topic → Entries)

User authentication & authorization

CRUD operations

URL routing

Template inheritance

Form handling using Django Forms

Deployment using Render

🗂️ Project Structure
learning_log/
│
├── learning_logs/        # Main application
├── users/                # Handles authentication
├── templates/            # HTML templates
├── db.sqlite3            # SQLite database
├── manage.py
└── requirements.txt
🛠️ Tech Stack

Python 3.12.8

Django 5.1

SQLite (default Django database)

Bootstrap 5

Render (deployment)

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/learning-log.git
cd learning-log
2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Apply migrations
python manage.py migrate
5️⃣ Run the development server
python manage.py runserver
Visit:
http://127.0.0.1:8000/

🔐 Authentication System

This project uses Django’s built-in authentication system to:

Register new users

Log in existing users

Restrict access to user-owned data

Protect views using login decorators

Each topic is linked to a specific user to ensure secure data separation.

📚 Database Design

User (Django default model)

Topic → linked to User (ForeignKey)

Entry → linked to Topic (ForeignKey)

This establishes a One-to-Many relationship:

One User → Many Topics

One Topic → Many Entries

🎯 Learning Goals of This Project

The purpose of this project was to:

Understand Django’s architecture

Practice backend development fundamentals

Implement authentication & authorization

Work with relational databases using Django ORM

Deploy a Django project to production

📎 GitHub Repository

🔗 https://github.com/syedriyyan9-cloud/Learning_Log

📌 Future Improvements

Add search functionality

Add pagination for entries

Add REST API using Django REST Framework

Switch to PostgreSQL in production

Improve UI/UX design