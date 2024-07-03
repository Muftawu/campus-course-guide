from django.contrib import admin
from .models import VideoResource, BookResource, LinkResource, ImageResource

admin.site.register(VideoResource)
admin.site.register(BookResource)
admin.site.register(LinkResource)
admin.site.register(ImageResource)