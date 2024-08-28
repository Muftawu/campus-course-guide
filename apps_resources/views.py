from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Tutorial
from django.urls import reverse
from helper.forms import TutorialForm, ResourceForm, EditProfileForm, Resource
from django.db.models import Q


@login_required(login_url='users:user_login')
def tutorials(request):
    user = request.user
    edit_profile_form = EditProfileForm(instance=user)
    tutorial_form = TutorialForm()
    student_tutorials = Tutorial.objects.all()
    resource_form = ResourceForm()
    tutorials = Tutorial.objects.filter(user=request.user)
    if request.method == "POST":
        if 'edit_profile' in request.POST:
            edit_profile_form = EditProfileForm(instance=user)
            user = EditProfileForm(data=request.POST, instance=user)
            if user.is_valid():
                user.save()
                messages.success(request, 'Profile updated successfully')
                return HttpResponseRedirect(reverse('users:dashboard')) 
    context = {'tutorials': tutorials, 'user_profile': edit_profile_form, 'tutorial_form': tutorial_form, 'resource_form': resource_form, 'student_tutorials': student_tutorials}
    return render(request, 'resources/tutorials.html', context)

@login_required(login_url='users:user_login')
def resources(request):
    user = request.user
    edit_profile_form = EditProfileForm(instance=user)
    tutorial_form = TutorialForm()
    student_tutorials = Tutorial.objects.all()
    resource_form = ResourceForm()
    tutorials = Tutorial.objects.filter(user=request.user)
    all_resources = Resource.objects.all()
    if request.method == "POST":
        if 'edit_profile' in request.POST:
            edit_profile_form = EditProfileForm(instance=user)
            user = EditProfileForm(data=request.POST, instance=user)
            if user.is_valid():
                user.save()
                messages.success(request, 'Profile updated successfully')
                return HttpResponseRedirect(reverse('users:dashboard')) 
    context = {'tutorials': tutorials, 'user_profile': edit_profile_form, 'tutorial_form': tutorial_form, 'resource_form': resource_form, 'student_tutorials': student_tutorials, 'all_resources': all_resources}
    return render(request, 'resources/all_resources.html', context)

@login_required(login_url='users:user_login')
def search_results(request, query):
    user = request.user
    edit_profile_form = EditProfileForm(instance=user)
    tutorial_form = TutorialForm()
    resource_form = ResourceForm()
    search_results = Resource.objects.filter(Q(resource_name__icontains=query) | Q(related_programmes__icontains=query) | Q(description__icontains=query))  
    context = {'search_results': search_results, 'query': query, 'user_profile': edit_profile_form, 'tutorial_form': tutorial_form, 'resource_form': resource_form}
    return render(request, 'resources/search_results.html', context)


