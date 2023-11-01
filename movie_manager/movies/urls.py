"movies urls"

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='c'),
    path('list/', views.List, name='l'),
    path('edit/', views.edit, name='e'),
    path('', views.edit, name='e'),
    
]
