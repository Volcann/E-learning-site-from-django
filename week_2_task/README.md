---

# E-Learning Django Project

## 1. CRUD Operations and Website Images

This project provides basic CRUD operations for managing `Course` and `Lecture` entities. The dashboard is the central place where users can view courses, add new courses, edit or delete them, and interact with associated lectures. Below is an overview of the CRUD operations and how they work in the system.

### **Dashboard**
The dashboard displays the list of available courses. Users can interact with each course and see its associated lectures.

![Dashboard](https://github.com/Volcann/E-learning-site-from-django/blob/d906d3aa123dcf033ba02427a48568de64ee7818/week_2_task/ss/dashboard.png)

---

### **Create Operations**:

- **Course Level**: This form allows users to add a new course by filling out the course name, description, and other relevant details.

![Course Level Image](https://github.com/Volcann/E-learning-site-from-django/blob/d906d3aa123dcf033ba02427a48568de64ee7818/week_2_task/ss/createCourse.png)

- **Lecture Level**: A similar form allows users to add a new lecture associated with an existing course.

---

### **Read Operations**:

- **Course List**: Displays a list of all courses available on the platform. Each course can be clicked to view its lectures.

![Course Level Image](https://github.com/Volcann/E-learning-site-from-django/blob/d906d3aa123dcf033ba02427a48568de64ee7818/week_2_task/ss/viewCourse.png)

- **Lecture List**: Displays all lectures associated with a specific course.

---

### **Update Operations**:

- **Course Update**: Users can edit course details, such as the name and description, using an update form.

![Course Level Image](https://github.com/Volcann/E-learning-site-from-django/blob/d906d3aa123dcf033ba02427a48568de64ee7818/week_2_task/ss/updateCourse.png)

---

### **Delete Operations**:

- **Course Deletion**: Users can delete a course via a simple button interface.

![Course Level Image](https://github.com/Volcann/E-learning-site-from-django/blob/d906d3aa123dcf033ba02427a48568de64ee7818/week_2_task/ss/deleteCourse.png)

---

## 2. Views, Models, and Forms

### **Models**:

In this section, we define the `Course` and `Lecture` models to structure the data for courses and lectures.

```python
# models.py

from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

- **Course Model**: Represents a course with a title, description, and creation timestamp.
- **Lecture Model**: Represents a lecture linked to a course, with a title, content, and timestamp.

---

### **Forms**:

To manage user input, we use Django forms to create and edit `Course` and `Lecture` objects.

```python
# forms.py

from django import forms
from .models import Course, Lecture

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['course', 'title', 'content']
```

These forms handle the validation and processing of user input for creating and updating courses and lectures.

---

### **Views**:

The views handle the business logic for displaying and managing courses and lectures. Below are examples of the views for creating courses and lectures.

```python
# views.py

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Course, Lecture
from .forms import CourseForm, LectureForm

def create_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/courses/')
    else:
        form = CourseForm()
    return render(request, 'create_course.html', {'form': form})

def create_lecture(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        form = LectureForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/courses/{}/lectures/'.format(course_id))
    else:
        form = LectureForm()
    return render(request, 'create_lecture.html', {'form': form, 'course': course})
```

These views handle the logic for creating courses and lectures, saving the data to the database, and redirecting users back to the appropriate pages.

---

## 3. Database Migration: SQLite to PostgreSQL

### **Steps for Migration**:

1. **Install PostgreSQL**: Ensure PostgreSQL is installed and running on your machine. Create a new database in PostgreSQL.

2. **Update `settings.py`**: In the Django project, change the database configuration to use PostgreSQL instead of SQLite. Modify the `DATABASES` setting as follows:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'mydatabase',
           'USER': 'myuser',
           'PASSWORD': 'mypassword',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

   - Replace `mydatabase`, `myuser`, and `mypassword` with the actual PostgreSQL database name, user, and password.

3. **Run Migrations**: Execute the following command to apply the migrations and set up the PostgreSQL database:
   
   ```
   python manage.py migrate
   ```

4. **Data Migration**: If you're migrating data from an existing SQLite database to PostgreSQL, you can use Django’s `dumpdata` and `loaddata` commands or write custom scripts to export and import the data.

   - **Export Data**: `python manage.py dumpdata > data.json`
   - **Import Data**: `python manage.py loaddata data.json`

   This will ensure that all the existing data from SQLite is successfully transferred to PostgreSQL.

---
