from django.db import models
from django.contrib.auth.models import User
from offsite_questions.models import Team

# Create your models here.

class User_Profile (models.Model):
    """Contains further information about the user."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_creator = models.BooleanField(default=False)
    team = models.ForeignKey(Team, on_delete=models.PROTECT)