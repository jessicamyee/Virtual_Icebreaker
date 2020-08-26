from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from offsite_questions.models import Entry
import random


def index(request):
    """The home page for Hotsprings Questions"""

    #GET request, hit the page for the first time
    if request.method == 'GET':
        context = {'question': ''}
      

    #POST request, the user has submitted something via the form
    elif request.method == 'POST':
        data = request.POST
        context = {'question': Entry.random_question()} 

    return render(request, 'offsite_questions/index.html', context)
