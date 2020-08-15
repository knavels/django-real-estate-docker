from django.contrib import messages, auth
from django.shortcuts import render, redirect
from secrets import compare_digest
from django.contrib.auth import get_user_model
from contacts.models import Contact


def register(request):
    """handles register page for registering users"""
    if request.method == 'POST':
        # Get from values
        full_name = request.POST['full_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if not compare_digest(password, password2):
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        # check username
        if get_user_model().objects.filter(email=email).exists():
            messages.error(request, 'there is already a user registered with given email address')
            return redirect('register')

        user = get_user_model().objects.create_user(email=email, name=full_name, password=password)
        
        # login after register
        # auth.login(request, user)
        # messages.success(request, 'You are registered successfully and now logged in')
        # return redirect('index')
        
        user.save()
        messages.success(request, 'You are registered successfully and can log in')
        return redirect('login')

    else:
        return render(request, 'accounts/register.html')


def login(request):
    """handles login page for signing in users"""
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(email=email, password=password)
        
        if user is None:
            messages.error(request, 'email and password mismatch')
            return redirect('login')
        
        auth.login(request, user)
        messages.success(request, 'You are now logged in')
        return redirect('dashboard')
        
        
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    """handles logout page for logging out users"""
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('login')


def dashboard(request):
    """handles dashboard page for showing inquiries to registered users"""
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contacts
    }

    return render(request, 'accounts/dashboard.html', context)
