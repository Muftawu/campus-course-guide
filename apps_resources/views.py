from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Tutorial
from helper.forms import TutorialForm, ResourceForm, EditProfileForm, Resource
from django.db.models import Q


@login_required(login_url='users:user_login')
def tutorials(request):
    user = request.user
    edit_profile_form = EditProfileForm(instance=user)
    tutorial_form = TutorialForm()
    resource_form = ResourceForm()
    tutorials = Tutorial.objects.filter(user=request.user)
    context = {'tutorials': tutorials, 'edit_profile_form': edit_profile_form, 'tutorial_form': tutorial_form, 'resource_form': resource_form}
    return render(request, 'resources/tutorials.html', context)

@login_required(login_url='users:user_login')
def search_results(request, query):
    user = request.user
    edit_profile_form = EditProfileForm(instance=user)
    tutorial_form = TutorialForm()
    resource_form = ResourceForm()
    search_results = Resource.objects.filter(Q(resource_name__icontains=query) | Q(related_programmes__icontains=query) | Q(description__icontains=query))  
    print('search results for ', query, search_results)       
    context = {'search_results': search_results, 'query': query, 'edit_profile_form': edit_profile_form, 'tutorial_form': tutorial_form, 'resource_form': resource_form}
    return render(request, 'resources/search_results.html', context)
