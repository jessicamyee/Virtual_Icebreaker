from django.contrib import admin
from .models import User_Profile
from import_export import resources
from app_users.models import User_Profile


# Register your models here.

class User_Profile(resources.ModelResource):
    class Meta:
        model = User_Profile