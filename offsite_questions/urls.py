"""Defines URL patterns for offsite_questions."""

from django.contrib import admin
from django.urls import path
from . import views



app_name = 'offsite_questions'
urlpatterns = [
    path('admin/', admin.site.urls),
    # Home page
    path('', views.index, name='index'),
]
