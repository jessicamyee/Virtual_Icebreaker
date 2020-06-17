from django.shortcuts import render

# <QueryDict: {
# 'csrfmiddlewaretoken': ['l3PWk42bp48JRSuhhN9mWpJcwg81JaGuxiolRiJdliXtMWHBiBKyKXg0cwSlxzQQ'],
# 'question_number': ['30'],
# 'submit': ['']}
# >


def index(request):
    """The home page for Offsite Hotsprings Questions"""
    question_list = {
        1: "Are you a boop?",
        2: "What kitchen appliance are you?",
        3: "Hotsprings are good?",
        4: "Can you get me boba?",
        5: 'Which came first. The chicken or the egg?',
    }

    # GET request, hit the page for the first time
    if request.method != 'POST':

        context = {'question': ''}

    # POST request, the user has submitted something via the form
    else:
        data = request.POST
        output = data['question_number']
        get_question = question_list[int(output)]
        context = {'question': get_question}

    return render(request, 'q2_hotsprings_temps/index.html', context)
