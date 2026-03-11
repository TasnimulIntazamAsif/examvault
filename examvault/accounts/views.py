from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from .models import User


def register_view(request):

    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'register.html', {'form': form})


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)

            if user.role == 'student':
                return redirect('student_dashboard')

            elif user.role == 'teacher':
                return redirect('teacher_dashboard')

            else:
                return redirect('admin_dashboard')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')