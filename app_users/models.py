from django.db import models
from django.contrib.auth.models import User
from offsite_questions.models import Team

# Create your models here.

class User_Profile (models.Model):
    """Relationship table to show which team is user is in"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
