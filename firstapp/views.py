from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from .models import Customer
from django.contrib import messages
from .forms import CustomerForm


def index(request):
    if request.user.is_authenticated:
        return render(request, "index.html", {"user": request.user})
    return redirect("login")


def error(request):
    return render(request, "error-404.html")


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or Password is Invalid')
            return redirect('login')
        
    else:
        return render(request, "login.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        password_two = request.POST["password_two"]

        if password == password_two:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Exists")
                return redirect("register")
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Exists")
                return redirect("register")
            else:
                # Create User instance
                user = User.objects.create_user(
                    username=username, password=password, email=email
                )
                user.save()
    
                # Create associated Customer instance
                customer = Customer.objects.create(
                    user=user,
                    name=name,
                    username=username,
                    password=password,
                    email=email,
                )
                customer.save()

                return redirect("login")
        else:
            messages.info(request, "Password Not the Same")
            return redirect("register")
    else:
        return render(request, "register.html")


@login_required
def profile(request):
    return render(request, "profile.html", {"user": request.user})


@login_required
def create_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user  # Link Customer to User
            customer.save()
            return redirect("profile")  # Redirect to profile or another page
    else:
        form = CustomerForm()
    return render(request, "create_customer.html", {"form": form})


def logout(request):
    auth_logout(request)
    return redirect("login")


## Some code for debugging
def some_view(request):
    if request.user.is_authenticated:
        try:
            customer = request.user.customer
            print(f"Customer name: {customer.name}")
        except Customer.DoesNotExist:
            print("No customer object for this user")
    return render(request, "your_template.html")
