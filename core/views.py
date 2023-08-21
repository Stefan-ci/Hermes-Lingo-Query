from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login

from accounts.models import User
from accounts.decorators import unauthenticated_user
from accounts.forms import LoginForm, CreateUserForm


def home_view(request):
    template_name = "home.html"
    return render(request, template_name)




@unauthenticated_user
def register_view(request):
    form = CreateUserForm
    if request.method == "POST":
        form = CreateUserForm(request.POST) or None
        
        if form.is_valid():
            cleaned_data = form.cleaned_data
            
            if User.objects.filter(email=cleaned_data["email"]).exists():
                messages.error(request, "Email address is already in use")
                return redirect(".")
            elif User.objects.filter(username=cleaned_data["username"]).exists():
                messages.error(request, "Username is already in use")
                return redirect(".")
            
            user = form.save()
            messages.success(request, "Account created successfully")
            
            # Loging in the new user
            auth_user = authenticate(request, email=user.email, password=user.password)
            if auth_user is not None and auth_user.is_active:
                login(request, user)
                if "next" in request.POST:
                    return redirect(request.POST.get("next"))
                return redirect("core:profile")
            
            else: # User is None or inactive
                messages.warning(request, "Oops! Failed to authenticate. Login manually please!")
                return redirect("core:home")
            
        else:  # if not form.is_valid()
            errors = form.errors.as_data()
            for error in errors:
                msg = "".join(errors[error][0])
                messages.error(request, f"{error.capitalize()}: {msg}")
            return redirect(".")
    
    else: # request.method != "POST"
        form = CreateUserForm()
    
    context = {"form": form}
    template_name = "register.html"
    return render(request, template_name, context)





@unauthenticated_user
def login_view(request):
    form = LoginForm
    
    if request.method == "POST":
        form = LoginForm(request.POST) or None
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            
            user = authenticate(request, email=email, password=password)
            if user is not None and user.is_active:
                login(request, user)
                messages.success(request, f"Welcome back, {request.user.username}")
                if "next" in request.POST:
                    return redirect(request.POST.get("next"))
                return redirect("core:profile")

            else: # User is None or inactive or wrong credentials
                messages.warning(request, "Oops! Wrong email or password!")
                return redirect(".")
        
        else:  # if not form.is_valid()
            errors = form.errors.as_data()
            for error in errors:
                msg = "".join(errors[error][0])
                messages.error(request, f"{error.capitalize()}: {msg}")
            return redirect(".")
    
    else: # request.method != "POST"
        form = LoginForm()
            
    context = {"form": form}
    template_name = "login.html"
    return render(request, template_name, context)





@login_required(login_url="core:login")
def profile_view(request):
    template_name = "profile.html"
    return render(request, template_name)



@login_required(login_url="core:login")
def logout_view(request):
    logout(request)
    messages.success(request, "Successfully logged out !")
    return redirect(request.META.get("HTTP_REFERER"))
