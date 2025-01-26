from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm
from .models import SuccessMetric, SuccessStory

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            send_mail(
                'Contact Us Message',  # Subject
                message,  # Message
                settings.DEFAULT_FROM_EMAIL,  # From email (set in settings.py)
                [settings.ADMIN_EMAIL],  # Admin email (set in settings.py)
                fail_silently=False,
            )
            return render(request, 'app1/dashboard.html')  # A thank-you page
    else:
        form = ContactForm()

    return render(request, 'app1/contact_us.html', {'form': form})

# Login View
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)  # Use Django's built-in login function
                messages.success(request, 'Login successful!')
                return redirect('dashboard')  # Redirect to the dashboard
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = UserLoginForm()
    return render(request, 'app1/new_login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Do not save immediately
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()  # Save the user with the hashed password
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'app1/signup.html', {'form': form})

def portfolio(request):
    success_metrics = SuccessMetric.objects.all()
    success_stories = SuccessStory.objects.all()
    return render(request, 'portfolio.html', {
        'success_metrics': success_metrics,
        'success_stories': success_stories
    })

def logout(request):
    auth_logout(request)  # Use Django's built-in logout function
    messages.success(request, 'Logged out successfully.')
    return render(request, 'app1/logout.html')

@login_required(login_url='login')  # Redirect to 'login' if user is not authenticated
def dashboard(request):
    return render(request, 'app1/dashboard.html')

def contact_us(request):
    return render(request, 'app1/contact_us.html')