from django.db import models
from helper.utils import *
import uuid
from apps_users.models import CustomUser
from multiselectfield import MultiSelectField

class Resource(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    resource_name = models.CharField(max_length=MAX_STR_LEN, null=True, blank=True)
    resource_type = models.CharField(max_length=MIN_STR_LEN, null=True, blank=True)
    related_programmes = MultiSelectField(choices=[(prog, prog) for prog in PROGRAMME], max_length=200, max_choices=15, null=True, blank=True)
    resource_item = models.FileField(upload_to='uploads', null=True, blank=True)
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
    

class Tutorial(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=MAX_STR_LEN, null=True, blank=True, verbose_name="Name of Tutorial")
    programme = MultiSelectField(choices=[(prog, prog) for prog in PROGRAMME], max_length=200, max_choices=15, null=True, blank=True, verbose_name="Related Programmes")
    topic = models.CharField(max_length=MAX_STR_LEN, null=True, blank=True)
    session = MultiSelectField(choices=[(sess, sess) for sess in SESSION], max_length=200, max_choices=15, null=True, blank=True)
    mode = models.CharField(max_length=MAX_STR_LEN, choices=[(mode, mode) for mode in TUTORIAL_MODES], null=True, blank=True, verbose_name="Mode of meeting")
    link = models.URLField(null=True, blank=True, verbose_name="Link to meeting if Online/Virtual")
    venue = models.CharField(max_length=MAX_STR_LEN, null=True, blank=True)
    date_and_time = models.DateTimeField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.venue} - @ {self.date_and_time}"
