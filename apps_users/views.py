from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from helper.forms import UserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from apps_resources.models import LinkResource, BookResource, ImageResource, VideoResource, BaseResource

def user_login(request):
    user = None
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {str(user).capitalize()}")
            return redirect("users:dashboard")
        else:
            messages.error(request, "Invalid credentials")

    context= {'user': user}
    return render(request, 'users/login.html', context)

def user_register(request):

    if request.user.is_authenticated:
        return redirect('users:dashboard')
    else:
        form = UserForm()
        if request.method == "POST":
            form = UserForm(request.POST)
            if form.is_valid():
                user = form.save()
                messages.success(request, f'{user} account created successfully')
                return redirect('users:user_login')
            else:
                messages.error(request, form.errors)
        else:
            form = UserForm()

        context = {'form': form}
        return render(request, 'users/register.html', context)

def welcome(request):
    context= {}
    return render(request, 'users/welcome.html', context)

def dashboard(request):
   
    if not request.user.is_authenticated:
        return redirect('users:user_login')
    recommended = ['CE 151', 'Calculus with Several Variables', 'Basic Mechanics', 'Operating System']
    ta_uploads = [f'Upload {i+1}' for i in range(5)]
    
    uploaded_resources = BaseResource.get_all_resources(request.user)
    print('uploaded resources', uploaded_resources)
    print("="*50)

    # context= {'recommended': recommended, 'uploads': ta_uploads}
    context= {'all_uploads': uploaded_resources}
    return render(request, 'users/dashboard.html', context)

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('users:welcome')
