from django.shortcuts import render,redirect
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def register_page(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('first_name')
            messages.success(request,'Account was created for ' + user)
            return redirect('login')
    context = {'form': form}
    return render(request,'authentication/register.html',context)


def login_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('')
        else:
            messages.info(request,'Email OR password is incorrect')

    context = {}
    return render(request,'authentication/login.html',context)


def log_out(request):
    logout(request)
    return redirect('login')