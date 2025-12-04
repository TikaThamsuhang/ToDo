================================================================================
                        DJANGO TO-DO APPLICATION
================================================================================

PROJECT DESCRIPTION
-------------------
This is a full-featured To-Do List application built with Django 4.1.7. 
The application allows users to manage their daily tasks with a modern, 
user-friendly interface. Users can create, edit, delete, and organize tasks 
by categories, set due dates, and track their completion status.

The application includes user authentication, profile management with avatar 
uploads, and a responsive design that works seamlessly across all devices.


KEY FEATURES
------------
✓ User Authentication (Register, Login, Logout)
✓ User Profile Management with Avatar Upload
✓ Create, Read, Update, Delete (CRUD) Tasks
✓ Task Categories (General, Work, Personal, Shopping, Health, Education)
✓ Due Date Tracking
✓ Mark Tasks as Complete/Incomplete
✓ User-specific Task Management (Users only see their own tasks)
✓ Responsive Design with Modern UI
✓ Media File Handling for User Avatars
✓ SQLite Database (Easy to set up and portable)


TECHNOLOGY STACK
----------------
- Backend: Django 4.1.7
- Database: SQLite3
- Frontend: HTML5, CSS3, JavaScript
- Authentication: Django's built-in authentication system
- File Uploads: Django's media handling


PREREQUISITES
-------------
Before running this project, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)
- Git (for cloning the repository)


================================================================================
                        INSTALLATION & SETUP GUIDE
================================================================================

STEP 1: CLONE THE REPOSITORY
-----------------------------
Open your terminal/command prompt and run:

    git clone https://github.com/TikaThamsuhang/ToDo.git
    cd todo


STEP 2: CREATE A VIRTUAL ENVIRONMENT
-------------------------------------
It's recommended to use a virtual environment to isolate project dependencies.

For Windows:
    python -m venv env
    env\Scripts\activate

For macOS/Linux:
    python3 -m venv env
    source env/bin/activate

You should see (env) in your terminal prompt, indicating the virtual 
environment is active.


STEP 3: INSTALL DEPENDENCIES
-----------------------------
Install all required packages using the requirements.txt file:

    pip install -r requirements.txt

This will install Django and all other necessary dependencies including:
- Django 4.1.7
- Pillow (for image handling)
- And other required packages


STEP 4: APPLY DATABASE MIGRATIONS
----------------------------------
Set up the database by running migrations:

    python manage.py makemigrations
    python manage.py migrate

This will create the SQLite database (db.sqlite3) and all necessary tables.


STEP 5: CREATE A SUPERUSER (ADMIN ACCOUNT)
-------------------------------------------
To access the Django admin panel and manage the application, create a 
superuser account:

    python manage.py createsuperuser

You will be prompted to enter:
- Username: (choose any username, e.g., admin)
- Email address: (optional, you can press Enter to skip)
- Password: (enter a secure password)
- Password (again): (confirm your password)

Example:
    Username: admin
    Email address: admin@example.com
    Password: ********
    Password (again): ********

Note: The password won't be visible as you type for security reasons.


STEP 6: RUN THE DEVELOPMENT SERVER
-----------------------------------
Start the Django development server:

    python manage.py runserver

The server will start at: http://127.0.0.1:8000/

You should see output like:
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.


STEP 7: ACCESS THE APPLICATION
-------------------------------
Open your web browser and navigate to:

    Main Application: http://127.0.0.1:8000/
    Admin Panel: http://127.0.0.1:8000/admin/

For the admin panel, use the superuser credentials you created in Step 5.


================================================================================
                        USING THE APPLICATION
================================================================================

FIRST-TIME USER REGISTRATION
-----------------------------
1. Go to http://127.0.0.1:8000/
2. Click on "Register" or "Sign Up"
3. Fill in the registration form:
   - Username
   - Email (optional)
   - Password
   - Confirm Password
4. Click "Register"
5. You'll be automatically logged in and redirected to the home page


MANAGING TASKS
--------------
Once logged in, you can:

1. ADD A NEW TASK:
   - Enter task description in the input field
   - Select a category (General, Work, Personal, etc.)
   - Set a due date (optional)
   - Click "Add Task"

2. EDIT A TASK:
   - Click the "Edit" button next to any task
   - Modify the task details
   - Click "Update Task"

3. MARK AS COMPLETE/INCOMPLETE:
   - Click the checkbox or "Complete" button to mark a task as done
   - Click "Undo" to mark it as incomplete

4. DELETE A TASK:
   - Click the "Delete" button next to the task
   - The task will be permanently removed


MANAGING YOUR PROFILE
----------------------
1. Click on "Profile" in the navigation menu
2. You can:
   - Update your username and email
   - Upload a profile avatar/picture
   - Add a bio (description about yourself)
3. Click "Update Profile" to save changes


================================================================================
                        ADMIN PANEL ACCESS
================================================================================

The Django admin panel provides advanced management capabilities:

1. Navigate to: http://127.0.0.1:8000/admin/
2. Log in with your superuser credentials
3. From here you can:
   - Manage all users
   - View and edit all tasks
   - Manage user profiles
   - Access Django's built-in user and group management


================================================================================
                        PROJECT STRUCTURE
================================================================================

todo/
├── manage.py                 # Django management script
├── db.sqlite3               # SQLite database file
├── requirements.txt         # Python dependencies
├── README.txt              # This file
├── DEPLOYMENT.md           # Deployment instructions
│
├── todo_main/              # Main project configuration
│   ├── settings.py         # Project settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI configuration
│
├── todo/                   # Main application
│   ├── models.py          # Database models (Task, UserProfile)
│   ├── views.py           # View functions
│   ├── forms.py           # Form definitions
│   ├── urls.py            # App URL patterns
│   └── admin.py           # Admin configuration
│
├── templates/              # HTML templates
│   ├── base.html          # Base template
│   ├── home.html          # Main task list page
│   ├── login.html         # Login page
│   ├── register.html      # Registration page
│   ├── profile.html       # User profile page
│   └── edit_task.html     # Task editing page
│
├── static/                 # Static files (CSS, JS, images)
│   └── css/
│       └── style.css      # Main stylesheet
│
└── media/                  # User-uploaded files
    └── avatars/           # User profile pictures


================================================================================
                        TROUBLESHOOTING
================================================================================

ISSUE: "No module named 'django'"
SOLUTION: Make sure your virtual environment is activated and run:
          pip install -r requirements.txt


ISSUE: "Table doesn't exist" error
SOLUTION: Run migrations:
          python manage.py makemigrations
          python manage.py migrate


ISSUE: "Port already in use"
SOLUTION: Either stop the other process using port 8000, or run on a 
          different port:
          python manage.py runserver 8080


ISSUE: Images not loading
SOLUTION: Make sure MEDIA_URL and MEDIA_ROOT are properly configured in 
          settings.py and that you've added media URL patterns in the main 
          urls.py file.


ISSUE: Static files not loading
SOLUTION: Run: python manage.py collectstatic
          Or check that STATIC_URL and STATICFILES_DIRS are properly 
          configured in settings.py


================================================================================
                        ADDITIONAL COMMANDS
================================================================================

CREATE MIGRATIONS (after model changes):
    python manage.py makemigrations

APPLY MIGRATIONS:
    python manage.py migrate

CREATE SUPERUSER:
    python manage.py createsuperuser

RUN DEVELOPMENT SERVER:
    python manage.py runserver

RUN ON DIFFERENT PORT:
    python manage.py runserver 8080

COLLECT STATIC FILES:
    python manage.py collectstatic

OPEN DJANGO SHELL:
    python manage.py shell

CHECK FOR ISSUES:
    python manage.py check


================================================================================
                        DEACTIVATING VIRTUAL ENVIRONMENT
================================================================================

When you're done working on the project, you can deactivate the virtual 
environment by running:

    deactivate


================================================================================
                        DEPLOYMENT
================================================================================

For deployment instructions to production servers (like PythonAnywhere, 
Heroku, or AWS), please refer to the DEPLOYMENT.md file included in this 
project.


================================================================================
                        SUPPORT & CONTRIBUTION
================================================================================

If you encounter any issues or have suggestions for improvements:
1. Check the troubleshooting section above
2. Review Django's official documentation: https://docs.djangoproject.com/
3. Feel free to contribute by submitting pull requests


================================================================================
                        LICENSE & CREDITS
================================================================================

This project was created as a learning exercise for Django web development.
Feel free to use, modify, and distribute this code for educational purposes.

Built with Django 4.1.7
Python 3.x


================================================================================
                        HAPPY TASK MANAGING! 🎯
================================================================================
