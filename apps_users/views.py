from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from helper.forms import UserForm
from django.contrib import messages

def user_login(request):
    context= {}
    return render(request, 'users/login.html', context)

def user_register(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'{user} account created successfully')
            return redirect('users:home')
        else:
            messages.error(request, form.errors)
    else:
        form = UserForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)

def landing_page(request):
    context= {}
    return render(request, 'users/landing_page.html', context)

def home(request):
    context= {}
    return render(request, 'users/home.html', context)
