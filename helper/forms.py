from django import forms 
from apps_users.models import CustomUser
from apps_resources.models import VideoResource, LinkResource, BaseResource, ImageResource


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "programme", "year", "college", "password"]
