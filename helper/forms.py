from django import forms 
from apps_users.models import CustomUser
from apps_resources.models import VideoResource, LinkResource, ImageResource, BookResource
from django.contrib.auth.forms import UserCreationForm 

class NewUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "programme", "year", "user_type", "password1", "password2"]
        
class EditProfile(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "programme", "year"]
        

class LinkResourceForm(forms.ModelForm):
    class Meta:
        model = LinkResource
        fields = "__all__"

class BookResourceForm(forms.ModelForm):
    class Meta:
        model = BookResource
        fields = "__all__"
        
class VideoResourceForm(forms.ModelForm):
    class Meta:
        model = VideoResource
        fields = "__all__"
        
class ImageResourceForm(forms.ModelForm):
    class Meta:
        model = ImageResource
        fields = "__all__"
        exclude = ["user", "slug", ]
        widgets = {
            'description': forms.Textarea(),
        }
