from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from .models import Customer
from django.contrib import messages
from .forms import CustomerUpdateForm, CustomerPasswordChangeForm


@login_required
def index(request):
    if request.user.is_authenticated:
        return render(request, "index.html", {"user": request.user})
    return redirect("login")


@login_required
def profile(request):
    customer = request.user.customer

    # Render the profile page with forms
    profile_form = CustomerUpdateForm(instance=customer)
    password_form = CustomerPasswordChangeForm(user=request.user)

    return render(
        request,
        "profile.html",
        {"profile_form": profile_form, "password_form": password_form},
    )


@login_required
def update_profile(request):
    customer = request.user.customer

    if request.method == "POST":
        form = CustomerUpdateForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully.")
            return redirect("profile")
        else:
            messages.error(request, "Please correct the error below.")

    return redirect("profile")


@login_required
def change_password(request):
    if request.method == "POST":
        form = CustomerPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password was successfully updated!")
            return redirect("profile")
        else:
            messages.error(request, "Please correct the error below.")

    return redirect("profile")


def custom_404(request):
    return render(request, "error-404.html", status=404)


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Username or Password is Invalid")
            return redirect("login")

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
def logout(request):
    auth_logout(request)
    return redirect("login")
