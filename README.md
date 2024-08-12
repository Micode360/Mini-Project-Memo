# Memo Management System

A simple Django project to manage memos with title, description, content, image, and video.

## Features
- Add new memos
- Upload images and videos
- View list of memos

## Prerequisites
- Python 3.x
- Django
- Pillow (for image handling)

## Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/yourusername/memo-management.git
    cd memo-management
    ```

2. **Create and activate a virtual environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**

    ```bash
    pip install django pillow
    ```

4. **Run migrations**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser to access the admin site**

    ```bash
    python manage.py createsuperuser
    ```

6. **Start the development server**

    ```bash
    python manage.py runserver
    ```

Open your browser and visit [http://127.0.0.1:8000/route](http://127.0.0.1:8000/route) to view the home page. 

Open your browser and visit [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) to log in to the admin site and manage memos. 
