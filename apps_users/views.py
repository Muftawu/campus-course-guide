from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from helper.forms import NewUserForm, CustomUser, EditProfile
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from django.urls import reverse
from apps_resources.models import LinkResource, BookResource, ImageResource, VideoResource, BaseResource

def user_login(request):
    if request.user.is_authenticated:
        return JsonResponse({'redirect' : reverse('users:dashboard')})
    
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        if not email or not password:
            return JsonResponse({'error': 'Please provide an email and a password'}, status=400)

        user = authenticate(request, email=request.POST["email"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            return JsonResponse({'redirect': reverse('users:dashboard'), 'message': f"Welcome back, {str(user).capitalize()}"})
        else:
            JsonResponse({'error': "Invalid credentials"}, status=400)
            
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def user_register(request):
    if request.user.is_authenticated:
        return redirect('users:dashboard')
    else:
        form = NewUserForm()
        if request.method == "POST":
            form = NewUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                messages.success(request, f'{user} account created successfully')
                return redirect('users:dashboard')
            else:
                messages.error(request, form.errors)
        else:
            form = NewUserForm()

def welcome(request):
    if request.user.is_authenticated:
        return redirect('users:dashboard')
    else:
        new_user_form = NewUserForm()
    context = {'new_user_form': new_user_form}
    return render(request, 'base.html', context)

@login_required(login_url='users:user_login')
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('users:user_login')
    
    context = {}
    form = None
    if request.user.user_type == "Teaching Assistant":
        uploaded_resources = BaseResource.get_all_resources(request.user)
        context.update({'all_uploads': uploaded_resources})
    else:
        recommended = ['CE 151', 'Calculus', 'Basic Mechanics', 'Operating System']
        context.update({'recommended': recommended})

    user = CustomUser.objects.get(slug=request.user.slug)
    if request.method == "POST":
        form = EditProfile(instance=user)
        user = EditProfile(data=request.POST, instance=user)
        if user.is_valid():
            user.save()
    else:
        form = EditProfile(instance=user)

    context.update({'user_profile': form})
    return render(request, 'users/dashboard.html', context)

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('users:welcome')
