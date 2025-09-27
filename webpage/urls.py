# webpage/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.creator_home, name='home'),
]