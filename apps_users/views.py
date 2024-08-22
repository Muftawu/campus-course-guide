from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from helper.forms import NewUserForm, CustomUser,  ResourceForm, EditProfileForm, Tutorial, TutorialForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from apps_resources.models import Resource
from django.urls import reverse
from django.db.models import Q 

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
            messages.success(request, f"Welcome back, {str(user.first_name).capitalize()}")
            return JsonResponse({'redirect': reverse('users:dashboard'), 'message': ''})
        else:
            JsonResponse({'error': "Invalid credentials"}, status=400)    

    return JsonResponse({'error': 'Invalid credentials or request method'}, status=400)

def user_register(request):
    if request.user.is_authenticated:
        return redirect('users:dashboard')
    
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully')
            return JsonResponse({'redirect': reverse('users:dashboard'), 'user': user.first_name})
        else:
            return JsonResponse({'error': f'{form.errors.as_data()}'}, status=400)
    else:
        form = NewUserForm()
    
    context = {}
    return render(request, 'users/dashboard.html', context)
    # return JsonResponse({'error': 'Invalid request method'}, status=400)

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
    if request.user.user_type == "Teaching Assistant":
        uploaded_resources = Resource.get_all_resources(user=request.user)
        context.update({'all_uploads': uploaded_resources})
    else:
        recommended = ['CE 151', 'Calculus', 'Basic Mechanics', 'Operating System']
        context.update({'recommended': recommended})

    user = CustomUser.objects.get(slug=request.user.slug)
    edit_profile_form = EditProfileForm(instance=user)
    tutorial_form = TutorialForm()
    resource_form = ResourceForm()
    
    if request.method == "POST":
        if 'edit_profile' in request.POST:
            edit_profile_form = EditProfileForm(instance=user)
            user = EditProfileForm(data=request.POST, instance=user)
            if user.is_valid():
                user.save()
                messages.success(request, 'Profile updated successfully')
                return HttpResponseRedirect(reverse('users:dashboard')) 

        elif 'resource_form' in request.POST:
            resource_form = ResourceForm(request.POST, request.FILES)
            if resource_form.is_valid():

                if request.FILES:
                    resource_obj = str(resource_form['resource_item'].data).split('.')
                    item = request.FILES['resource_item']
                else:
                    resource_obj = ["link", "link"]
                    item = None
                
                Resource.objects.create(
                    user=request.user,
                    resource_name=request.POST['resource_name'],
                    resource_type=resource_obj[-1],
                    related_programmes=request.POST['related_programmes'],
                    description=request.POST['description'],
                    resource_item=item,
                    resource_link=request.POST["resource_link"],
                )
                messages.success(request, 'Resource uploaded successfully')
                return HttpResponseRedirect(reverse('users:dashboard'))
            else:
                messages.error(request, f'{resource_form.errors.as_text()}')

        elif 'schedule_tutorial' in request.POST:
            tutorial_form = TutorialForm(request.POST)
            if tutorial_form.is_valid():
                tutorial = tutorial_form.save(commit=False)
                tutorial.user = user
                tutorial.save()
                messages.success(request, 'Tutorial successfully scheduled')
                return HttpResponseRedirect(reverse('resource:tutorials'))
            else:
                messages.error(request, f'{tutorial_form.errors.as_text()}')

        elif 'query' in request.POST:
            query = request.POST['search_item']
            # search_results = Resource.objects.filter(Q(resource_name__icontains=query) | Q(related_programmes__icontains=query) | Q(description__icontains=query))         
            # messages.success(request, 'Tutorial successfully scheduled')
            return HttpResponseRedirect(reverse('resource:search_results', args=[query]))

    else:
        edit_profile_form = EditProfileForm(instance=user)
        resource_form = ResourceForm()
        tutorial_form = TutorialForm(request.POST)

    context.update({'user_profile': edit_profile_form, 'resource_form': resource_form, 'tutorial_form': tutorial_form})
    return render(request, 'users/dashboard.html', context)

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect(reverse('users:welcome'))
