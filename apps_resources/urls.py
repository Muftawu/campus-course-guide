from django.urls import path
from . import views

app_name = "resource"

urlpatterns = [
    path('contributions/', views.tutorials  , name='contributions'),
]