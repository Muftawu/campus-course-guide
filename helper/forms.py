from django import forms 
from apps_users.models import CustomUser
from apps_resources.models import Resource, Tutorial
from django.contrib.auth.forms import UserCreationForm 

class NewUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "programme", "year", "user_type", "password1", "password2"]
        
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "programme", "year"]

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = "__all__"
        exclude = ["user", "slug", "resource_type",]

class EditResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = "__all__"
        exclude = ["user", "slug", "resource_type",]

class TutorialForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = ["name", "programme", "topic", "session", "venue", "mode", "link", "date_and_time"]
        widgets = {
            'date_and_time': forms.DateInput(attrs={'type': 'date'}),
        }