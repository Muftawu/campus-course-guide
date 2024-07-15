from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from helper.forms import LinkResourceForm, VideoResourceForm, ImageResourceForm, BookResourceForm
from django.contrib import messages

@login_required(login_url='users:user_login')
def upload_resource(request):
    forms_dict = {'link': LinkResourceForm, 'video': VideoResourceForm, 'image': ImageResourceForm, 'slide': BookResourceForm}
    form = forms_dict['image']
    
    if request.method == "POST":
        form = form(request.POST, request.FILES)
        if form.is_valid():
            resource =  form.save(commit=False)
            resource.user = request.user
            resource.save()

            messages.success(request, f'Resoruce {resource} uploaded successfully')
            return redirect('users:dashboard')
        else:
            messages.error(request, 'Error uploading resource. Try again')
    else:
        form = form
    context = {'form': form}
    return render(request, 'resources/resource_upload.html', context)