from django.urls import path
from . import views

app_name = "resource"

urlpatterns = [
    path('tutorials/', views.tutorials  , name='tutorials'),
    path('search_results/<str:query>/', views.search_results  , name='search_results'),
    path('all_resources/', views.resources, name='all_resources'),
]