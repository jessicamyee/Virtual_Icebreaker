from django.shortcuts import render
from offsite_questions.models import Entry


def index(request):
    """The home page for Hotsprings Questions"""

    #GET request, hit the page for the first time
    if request.method == 'GET':
        context = {'question': ''}

    #POST request, the user has submitted something via the form
    elif request.method == 'POST':
        data = request.POST
        entered_question_number = int(data['question_number'])

        question_text = Entry.objects.get(question_number = entered_question_number).question_text
        context = {'question': question_text}

    return render(request, 'q2_hotsprings_temps/index.html', context)

 
##Allowing users to add additional questions w/o needing to input a number. THe backend will just add an unused number ID to the new question
# ##Ensuring that we cannot add a question number when the number has been added

