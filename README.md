# Real Estate Listing Web Application

## Overview

This project is a web application for listing and browsing real estate properties. It is built using Django for the backend, Tailwind CSS for styling, and Flowbite for UI components.

## Features

- User authentication (registration, login, logout)
- CRUD functionality for real estate listings
- Display locations on a map
- Search and filter listings by various criteria
- Modern UI components using Flowbite

## Tech Stack

- **Backend**: Django
- **Frontend**: Tailwind CSS, Flowbite
- **Database**: Postgresql

## Installation

### Prerequisites

- Python 3.x
- Node.js and npm (for Tailwind CSS)
- Git
- PostgreSQL

### Steps

1. **Clone the repository:**
   ```bash
   git clone git@github.com:DagmawiSolomon/realestatelistingwebapp.git
   cd RealEstateApp
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install backend dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install frontend dependencies:**
   ```bash
   npm install
   ```

5. **Set up PostgreSQL database:**
   - Create a new PostgreSQL database and user:
     ```sql
     CREATE DATABASE your_database_name;
     CREATE USER your_database_user WITH PASSWORD 'your_database_password';
     ```
   - Update the `DATABASES` setting in `realestate/settings.py` with your PostgreSQL credentials:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'your_database_name',
             'USER': 'your_database_user',
             'PASSWORD': 'your_database_password',
             'HOST': 'localhost',  # or the address of your database server
             'PORT': '5432',
         }
     }
     ```

6. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Compile Tailwind CSS:**
   ```bash
   npx tailwindcss -i app/static/src/input.css -o app/static/src/output.css --watch
   ```

## Usage

### Creating a Superuser

To access the Django admin panel, you need to create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to create a superuser account.

### Running the Application

After setting up the project, you can start the development server:

```bash
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000/` to see the application in action.


