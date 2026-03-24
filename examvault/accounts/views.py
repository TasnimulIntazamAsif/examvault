from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
from .models import User


def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            messages.success(request, "Account created successfully!")

            return redirect('login')

        else:
            messages.error(request, "Something went wrong. Check your inputs.")

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)

            # Role-based redirect
            if user.role == 'student':
                return redirect('student_dashboard')

            elif user.role == 'teacher':
                return redirect('teacher_dashboard')

            else:
                return redirect('/admin/')

        else:
            messages.error(request, "Invalid username or password!")

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')