# Realestate listing webapp

### Overview

This project is a web application for listing and browsing real estate properties. It is built using Django for the backend, Tailwind CSS for styling, and Flowbite for UI components.

### Features

User authentication (registration, login, logout)
CRUD functionality for real estate listings
Search and filter listings by various criteria
Responsive design for mobile and desktop views
Modern UI components using Flowbite

Certainly! Below is a sample README for a real estate listing web application built with Django, Tailwind CSS, and Flowbite.

---

# Real Estate Listing Web Application

## Overview

This project is a web application for listing and browsing real estate properties. It is built using Django for the backend, Tailwind CSS for styling, and Flowbite for UI components.

## Features

- User authentication (registration, login, logout)
- CRUD functionality for real estate listings
- Display locations on a map
- Search and filter listings by various criteria
- Modern UI components using Flowbite

## Instalation

Certainly! Below is the updated README with the fixed third feature and a slight improvement to the formatting.

---

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
- **Database**: SQLite (default for Django, can be configured for PostgreSQL, MySQL, etc.)
- **Deployment**: [Your deployment method, e.g., Heroku, Docker, etc.]

## Installation

### Prerequisites

- Python 3.x
- Node.js and npm (for Tailwind CSS)
- Git

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

5. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Compile Tailwind CSS:**
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


