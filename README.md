# Attendance System (Django Project) 
This is a simple Django-based attendance management system. It allows you to manage students and record their attendance for each day. 

---------------------------------------------------------- 

## Project Contents and Explanation 

### 1. attendance_system/
This is the main Django project folder. 
It contains: 
- **settings.py** – Main configuration file for the project. 
- **urls.py** – Defines the global URL routes. 
- **wsgi.py / asgi.py** – Server deployment files. These files make sure Django knows how to run the project. 

---------------------------------------------------------- 

### 2. portal/ 
This is the main app of the project. It contains the core logic. 
Inside this folder: 

#### **a. models.py** 
Contains two models: 
- **Student** – Stores student information (name, active status). 
- **Attendance** – Stores attendance records for each student for a specific date. These models create tables in the database. 

#### **b. views.py** 
Contains all the functions that run the website: 
- Show home page 
- Display list of students 
- Mark attendance 
- Save attendance 
- Update old attendance 
- Display records Each function handles a specific page. 

#### **c. urls.py** 
Contains URL patterns for the portal. Links each page to its view. 

#### **d. templates/portal/** 
Contains HTML files: 
- **home.html** – Landing page 
- **attendance.html** – Marking attendance page 
- **update.html** – Update attendance page 
- **display.html** – Shows attendance table These are the frontend pages the user sees. 

#### **e. static/portal/** 
Contains: 
- **style.css** – Basic CSS for layout 

---------------------------------------------------------- 

### **3. db.sqlite3** 
This is the database file where all student records and attendance entries are stored. 

---------------------------------------------------------- 

### **4. manage.py** 
This file allows you to: 
- Run the server 
- Run migrations 
- Create superusers 
- Perform Django commands 

---------------------------------------------------------- 

## Working 
1. **Students are stored in the database** 
When the project runs, it loads students from the Student model. 

2. **Attendance marking** 
The attendance page shows all active students. You choose: **Present, Absent, or Leave** for each student. 

3. **Saving attendance** 
When you press save: - The system stores each student's attendance for that date in the Attendance table. 

4. **Updating attendance** 
If attendance already exists for a date, you can edit and save it again. 

5. **Displaying attendance** 
You can pick a date and see all attendance saved for that day. 

---------------------------------------------------------- 

##  Running the Project 

### Step 1 — Create Virtual Environment
python -m venv env

### Step 2 — Activate It Windows:
env\Scripts\activate

### Step 3 — Install Django
pip install django

### Step 4 — Migrate Database
python manage.py migrate

### Step 5 — Start Server
python manage.py runserver

---------------------------------------------------------- 
