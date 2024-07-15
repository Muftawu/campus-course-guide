from django.db import models
from helper.utils import *
import uuid
from apps_users.models import CustomUser
from multiselectfield import MultiSelectField

class BaseResource(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    resource_name = models.CharField(max_length=MAX_STR_LEN, null=True, blank=True)
    related_programmes = MultiSelectField(choices=[(prog, prog) for prog in PROGRAMME], max_length=200, max_choices=15, null=True, blank=True)
    description = models.CharField(max_length=MAX_STR_LEN, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-updated"]

    @classmethod
    def get_all_resources(cls, user):
        out = []
        try:
            out = cls.objects.filter(user=user)
        except:
            pass 
        return out 
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = uuid.uuid4()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.resource_name
    

class VideoResource(BaseResource):
    resource_item = models.FileField(upload_to='video_files', null=True, blank=True)

class BookResource(BaseResource):
    resource_item = models.FileField(upload_to='book_files', null=True, blank=True)

class LinkResource(BaseResource):
    resource_item = models.CharField(max_length=MAX_STR_LEN, null=True, blank=True)

class ImageResource(BaseResource):
    resource_item = models.ImageField(upload_to="images", null=True, blank=True)
 