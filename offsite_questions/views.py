from django.shortcuts import render
from offsite_questions.models import Entry

# <QueryDict: {
# 'csrfmiddlewaretoken': ['l3PWk42bp48JRSuhhN9mWpJcwg81JaGuxiolRiJdliXtMWHBiBKyKXg0cwSlxzQQ'],
# 'question_number': ['30'],
# 'submit': ['']}
# >

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
 
##Add some code where the first letter of the first word in the hotspring question is capitalized --- will also be its own unit test
##Ensuring submission integers are between 1-25 
##Ensuring that we cannot add a question number when the number has been added
##Will need to write another function in index.html where if a user submits a new hotsprings question, the min and max will increase by increment of 1 and the HTML hard-coding will not be static --- will unit test
