from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('user_login/', views.user_login, name='user_login'),
    path('user_register/', views.user_register, name='user_register'),
    path('landing_page/', views.landing_page, name='landing_page'),
    path('home/', views.home, name='home'),
]   