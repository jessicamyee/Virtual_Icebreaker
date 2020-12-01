from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import Registration
from offsite_questions.models import Team
from app_users.models import User_Profile

# Create your views here.

def logout_view(request):
    """Log the user out."""
    logout(request)
    return HttpResponseRedirect(reverse('offsite_questions:index'))


def register(request):
    """Register a new user."""
    if request.method != 'POST':
        #Display blank registration form.
        form = Registration() 

    else:
        #Process completed form.
        form = Registration(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            
            #Links team name to Teams table
            team = Team(team_name=form.cleaned_data.get("team_name"))
            team.save()

            #Links team to the user
            user_team = User_Profile(user=new_user, team=team)
            user_team.save()

            # Log the user in and then redirect to home page.
            authenticated_user= authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('offsite_questions:index'))

    context = {'form': form}
    return render(request, 'app_users/register.html', context)
    
