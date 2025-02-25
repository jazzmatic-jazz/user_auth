from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm
from .models import User, Address
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    return render(request, "user_auth/index.html")

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "user_auth/register.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            print(user, "user")
            if user.user_type == "1":
                return redirect("doctor")
            elif user.user_type == "2": 
                return redirect("patient")
            else:
                messages.error(request, "Invalid user type.")
                return redirect("login")  
    return render(request, "user_auth/login.html")


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required()
def doctor_dashboard(request):
    if request.user.user_type == "1":
        user = request.user
        get_user = User.objects.get(email=user)
        get_add = Address.objects.get(user_id=get_user.id)
        address = f"{get_add.line1}, {get_add.city}, {get_add.state}, {get_add.pin_code}"

        data = {
            "first_name": get_user.first_name,
            "last_name": get_user.last_name,
            "email": get_user.email,
            "address": address
        }
        return render(request, "user_auth/doc_dash.html", {"user": data})
    return render(request, "user_auth/index.html")

@login_required
def patient_dashboard(request):
    if request.user.user_type == "2":
        user = request.user
        get_user = User.objects.get(email=user)
        get_add = Address.objects.get(user_id=get_user.id)
        address = f"{get_add.line1}, {get_add.city}, {get_add.state}, {get_add.pin_code}"

        data = {
            "first_name": get_user.first_name,
            "last_name": get_user.last_name,
            "email": get_user.email,
            "username": get_user.username,
            "address": address
        }
       
        return  render(request, "user_auth/pat.html", {"user": data})
    return render(request, "user_auth/index.html")

