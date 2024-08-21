from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='users:user_login')
def tutorials(request):
    context = {}
    return render(request, 'resources/tutorials.html', context)

