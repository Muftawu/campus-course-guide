from django import forms 
from apps_users.models import CustomUser
from apps_resources.models import Resource
from django.contrib.auth.forms import UserCreationForm 
#Import tutorial class
from apps_resources.models import Tutorial

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


#create modelform to handle tutorial posts
class TutorialForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = ["name", "programme", "topic", "session", "venue", "date_and_time"]