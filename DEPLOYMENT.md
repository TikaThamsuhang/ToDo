# PythonAnywhere Deployment Guide

## Prerequisites
- GitHub account (to upload your code)
- PythonAnywhere free account

---

## Step 1: Create Requirements File

Create `requirements.txt` in your project root:
```
Django==4.1
Pillow
```

---

## Step 2: Prepare Your Code for Production

### Update `settings.py`:
```python
# Add your PythonAnywhere domain to ALLOWED_HOSTS
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com', 'localhost', '127.0.0.1']

# Keep DEBUG = False in production (change before deploying)
DEBUG = False

# Static files configuration
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

---

## Step 3: Push Code to GitHub

```bash
# Initialize git (if not already done)
git init
git add .
git commit -m "Prepare for deployment"

# Create a new repository on GitHub, then:
git remote add origin https://github.com/yourusername/your-repo.git
git branch -M main
git push -u origin main
```

---

## Step 4: Sign Up for PythonAnywhere

1. Go to https://www.pythonanywhere.com/
2. Click "Pricing & signup"
3. Choose "Create a Beginner account" (FREE)
4. Complete registration

---

## Step 5: Clone Your Repository

1. Go to PythonAnywhere Dashboard
2. Click "Consoles" → "Bash"
3. Run:
```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo/todo
```

---

## Step 6: Create Virtual Environment

```bash
mkvirtualenv --python=/usr/bin/python3.10 myenv
pip install -r requirements.txt
```

---

## Step 7: Configure Database

```bash
python manage.py migrate
python manage.py createsuperuser
```

---

## Step 8: Collect Static Files

```bash
python manage.py collectstatic
```

---

## Step 9: Set Up Web App

1. Go to "Web" tab
2. Click "Add a new web app"
3. Choose "Manual configuration"
4. Select Python 3.10
5. Click through the wizard

---

## Step 10: Configure WSGI File

1. In "Web" tab, click on WSGI configuration file
2. Delete everything and replace with:

```python
import os
import sys

# Add your project directory to the sys.path
path = '/home/yourusername/your-repo/todo'
if path not in sys.path:
    sys.path.append(path)

# Set environment variable for Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'todo_main.settings'

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**Replace `yourusername` and `your-repo` with your actual values!**

---

## Step 11: Set Virtual Environment

1. In "Web" tab, find "Virtualenv" section
2. Enter: `/home/yourusername/.virtualenvs/myenv`

---

## Step 12: Configure Static Files

In "Web" tab, add static files mapping:
- URL: `/static/`
- Directory: `/home/yourusername/your-repo/todo/staticfiles`

Add media files mapping:
- URL: `/media/`
- Directory: `/home/yourusername/your-repo/todo/media`

---

## Step 13: Update Settings

1. Go back to Bash console
2. Edit settings.py:
```bash
nano todo_main/settings.py
```

3. Update:
```python
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']
DEBUG = False
```

---

## Step 14: Reload Web App

1. Go to "Web" tab
2. Click the big green "Reload" button
3. Visit: `https://yourusername.pythonanywhere.com`

---

## Troubleshooting

### Error Logs
- Check error log in "Web" tab → "Log files"

### Common Issues

**Static files not loading:**
```bash
python manage.py collectstatic --noinput
```

**Database errors:**
```bash
python manage.py migrate
```

**Code changes not reflecting:**
- Always click "Reload" button after changes

---

## Updating Your App

When you make changes:
```bash
# On PythonAnywhere Bash console
cd ~/your-repo/todo
git pull origin main
python manage.py collectstatic --noinput
python manage.py migrate
# Then reload web app from Web tab
```

---

## Free Tier Limitations

- 1 web app
- 512 MB disk space
- Custom domain not included (use yourusername.pythonanywhere.com)
- No HTTPS for custom domains
- CPU time limits

---

## Success! 🎉

Your Django To-Do app is now live at:
`https://yourusername.pythonanywhere.com`
