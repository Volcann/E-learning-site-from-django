from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Lecture
from .forms import CourseForm, LectureForm

# Create Views
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'app2/course_create.html', {'form': form})

def lecture_create(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = LectureForm(request.POST)
        if form.is_valid():
            lecture = form.save(commit=False)
            lecture.course = course
            lecture.save()
            return redirect('course_detail', course_id=course.id)
    else:
        form = LectureForm()
    return render(request, 'app2/lecture_create.html', {'form': form, 'course': course})

# Read Views

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'app2/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    lectures = course.lectures.all()
    return render(request, 'app2/course_detail.html', {'course': course, 'lectures': lectures})

# Update Views

def course_update(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_detail', course_id=course.id)
    else:
        form = CourseForm(instance=course)
    return render(request, 'app2/course_update.html', {'form': form, 'course': course})

def lecture_update(request, lecture_id):
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    if request.method == 'POST':
        form = LectureForm(request.POST, instance=lecture)
        if form.is_valid():
            form.save()
            return redirect('course_detail', course_id=lecture.course.id)
    else:
        form = LectureForm(instance=lecture)
    return render(request, 'app2/lecture_update.html', {'form': form, 'lecture': lecture})

# Delete Views

def course_delete(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'app2/course_delete.html', {'course': course})

def lecture_delete(request, lecture_id):
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    if request.method == 'POST':
        lecture.delete()
        return redirect('course_detail', course_id=lecture.course.id)
    return render(request, 'app2/lecture_delete.html', {'lecture': lecture})