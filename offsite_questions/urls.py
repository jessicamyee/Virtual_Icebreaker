"""Defines URL patterns for offsite_questions."""

from django.urls import path
from . import views
app_name = 'offsite_questions'
urlpatterns = [
    # Home page
    path('', views.index, name='index')
]
