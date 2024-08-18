from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages

@login_required(login_url='users:user_login')
def upload_resource(request):
    return JsonResponse({'message': 'Hello Upload Resource Page'})
   