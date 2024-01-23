from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import registration_form, user_profile
from django.contrib.auth.forms import AuthenticationForm
from .models import userProfile


# Create your views here.

# Home page
def home(request):
    return render(request, 'home.html')


# Login function
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            person = authenticate(request, username=username, password=password)
            if person is not None:
                login(request, person)
                return redirect('landing_page')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'login_user.html', context)


# Registration Function
def register_user(request):
    if request.method == 'POST':
        form = registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = registration_form()
    context = {'form': form, }
    return render(request, 'register_user.html', context)


# Landing page after user login
@login_required(login_url='login_user')
def landing_page(request):
    details = userProfile.objects.filter(profile=request.user)
    context = {'details': details}
    return render(request, 'landing_page.html', context)


# Logout function
def logout(request):
    auth.logout(request)
    return redirect('home')


@login_required(login_url='login_user')
# Add User details
def profile_view(request):
    if request.method == 'POST':
        form = user_profile(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = request.user
            post.date_of_birth = form.cleaned_data['date_of_birth']
            post.full_name = form.cleaned_data['full_name']
            post.save()
            return redirect('landing_page')
    else:
        form = user_profile()
    context = {'form': form}
    return render(request, 'profile_view.html', context)
