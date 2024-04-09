from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .forms import CreateUserForm
from .decorators import unauthenticated_user, allowed_users


# Create your views here.
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account was created successfully.")
            return redirect("login")

    context = {'form':form}
    return render(request, "accounts/register.html", context)


@unauthenticated_user
def loginPage(request):
    
    if request.method == "POST":
        login_data = request.POST.get("login")
        password =request.POST.get("password")

        user = authenticate(request, username=login_data, password=password)
        print(user)
        print(user.user_type)

        if user is not None:
            login(request, user)
            if user.user_type == 'ADMIN':
                return redirect('home')
            elif user.user_type == 'SUPPLIER':
                return redirect('supplier_dashboard')
            elif user.user_type == 'CUSTOMER':
                return redirect('customer_dashboard')
        else:
            messages.info(request, "Invalid login credentials.")
        
    context = {}
    return render(request, "accounts/login.html", context)


def logoutUser(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def home(request):
    return render(request, "accounts/index.html")


@login_required(login_url="login")
@allowed_users(allowed_type="ADMIN")
def adminDashboard(request):
    return render(request, "accounts/admin_dashboard.html")


@login_required(login_url="login")
@allowed_users(allowed_type="CUSTOMER")
def customerDashboard(request):
    return render(request, "accounts/customer_dashboard.html")


@login_required(login_url="login")
@allowed_users(allowed_type="SUPPLIER")
def supplierDashboard(request):
    return render(request, "accounts/supplier_dashboard.html")
