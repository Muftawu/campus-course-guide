from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib import messages
from helper.forms import TutorialForm
from django.urls import reverse

@login_required(login_url='users:user_login')
def upload_resource(request):
    return JsonResponse({'message': 'Hello Upload Resource Page'})


#To handle tutorials posted, saving it to the database
def handleTutorialPost(request):

    # create object of form
    form = TutorialForm(request.POST or None, request.FILES or None)
     
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
    return HttpResponseRedirect(reverse("dashboard"))