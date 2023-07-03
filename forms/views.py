from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm
import datetime
import pytz

# Create your views here.


def registration_form(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form_data = form.cleaned_data

            # Create User object
            user = User.objects.create_user(
                username=form_data['username'],
                password=form_data['password']
            )

            # Create Biodata object and associate it with the User
            biodata = Biodata.objects.create(
                user=user,
                first_name=form_data['first_name'],
                other_names=form_data['other_names'],
                gender=form_data['gender'],
                phone_number=form_data['phone_number'],
                date_of_birth=form_data['date_of_birth'],
                email_address=form_data['email_address'],
                password=form_data['password'],
                username=form_data['username'],
                state_of_origin=form_data['state_of_origin'],
                school_name=form_data['school_name'],
                courses=form_data['courses'],
                any_programming_skill=form_data['any_programming_skill'],
                choose_internship_type=form_data['choose_internship_type'],
                number_of_months=form_data['number_of_months'],
                start_date=form_data['start_date'],
                end_date=form_data['end_date'],
                upload_photo=request.FILES.get('upload_photo'),
                upload_it_letter=request.FILES.get('upload_it_letter')
            )
            biodata.save()
            messages.info(request, 'Registration Succesfully. Check Your Dashboard Status for Apporval')
            return redirect('student_login')  # Replace 'student_login' with the actual name/url of your login page
        else:
            # Form is not valid, print the errors
            print(form.errors)
    else:
        form = StudentRegistrationForm()
    return render(request, 'registration.html', {'form': form})

def signOut(request):
    logout(request)
    return redirect('student_login')

def student_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('student_profile')
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
        
@login_required
def student_update(request):
    if request.method == 'POST':
        form = BiodataForm(request.POST, request.FILES, instance=request.user.biodata)
        if form.is_valid():
            form.save()
            
            return redirect('student_profile')
    else:
        form = BiodataForm(instance=request.user.biodata) 
    
    return render(request, 'update_student.html', {'form': form})
    
def Contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Additional form validation and processing logic can be added here

        send_mail(
            'Contact Form Submission',
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            settings.DEFAULT_FROM_EMAIL,
            ['hubemail@gmail.com'],
            fail_silently=False,
        )

        return render(request, 'contact_success.html', {'success': True})

    return render(request, 'contact.html')

def contact_success(request):
    return render(request, 'contact_success.html')
    

@login_required
def student_profile(request):
    try:
        biodata = Biodata.objects.get(user=request.user)
        return render(request, 'profile.html', {'biodata': biodata})
    except Biodata.DoesNotExist:
        
        return render(request, 'profile.html', {'error_message': 'No biodata available'}, context)