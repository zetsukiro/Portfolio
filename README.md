
# Portfolio Website (Django Project)

This is a simple Django-based portfolio website. It displays personal information, projects, skills, and other details using Django templates, views, and static files.

--------------------------------------------------------------------------------

## Project Contents

### 1. portfolioProject/
Main Django project folder. Contains:
- **settings.py** – Project settings  
- **urls.py** – Main URL routes  
- **wsgi.py / asgi.py** – Server files  

These files help Django run the project.

--------------------------------------------------------------------------------

### 2. main/
Main app of the portfolio website.

#### a. models.py
Contains the database structure (if used).  
Some portfolio projects may not require models.

#### b. views.py
Handles the logic for each page.  
Examples:
- Home page  
- About page  
- Projects page  
- Contact page  

#### c. urls.py
Connects each page to its corresponding view.

#### d. templates/main/
HTML templates that display the website’s content.

#### e. static/main/
Static files such as:
- CSS  
- JS  
- Images  

Used for page styling and design.

--------------------------------------------------------------------------------

### 3. db.sqlite3
Database file (if any models store data).  
Can be used for dynamic content.

--------------------------------------------------------------------------------

### 4. manage.py
Used for running the server, migrations, and managing the project through Django commands.

--------------------------------------------------------------------------------

## How It Works (Simple)

1. The user visits pages like home, about, skills, and projects.  
2. Django loads the templates from the `main/templates` folder.  
3. Static files (CSS/images) are loaded from `main/static`.  
4. Views connect the templates with any required data.

--------------------------------------------------------------------------------

## How to Run the Project

### Step 1 – Create Virtual Environment
python -m venv env

--------------------------------------------------------------------------------


### Step 2 – Activate It
env\Scripts\activate
OR

1. Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
Then 
2. env\Scripts\activate

--------------------------------------------------------------------------------

### Step 3 – Install Django
pip install django

--------------------------------------------------------------------------------

### Step 4 – Run Server
python manage.py runserver

--------------------------------------------------------------------------------

