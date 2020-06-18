from django.shortcuts import render

# <QueryDict: {
# 'csrfmiddlewaretoken': ['l3PWk42bp48JRSuhhN9mWpJcwg81JaGuxiolRiJdliXtMWHBiBKyKXg0cwSlxzQQ'],
# 'question_number': ['30'],
# 'submit': ['']}
# >


def index(request):
    """The home page for Offsite Hotsprings Questions"""
    question_list = {
        1: "What is one quality you do not want a mini you (could be a child or pet (?)) to inherit from you?",
        2: "What occupation would you excel in that is not your current OR previous job?",
        3: "If you could determine your own work schedule and did not have to worry about needing to work more or less due to your schedule, what would it look like? (ex: only work 2 days a week, between 1am-3am)",
        4: "What’s your favorite café drink and why?",
        5: "If you were a candy, what candy would you be?",
        6: "What is one thing you bought that you regret a lot?",
        7: "If you had to pass down an item you own to many generations, what item would that be?",
        8: "What’s your favorite useless superpower?",
        9: "What was the first thing you bought with your own money?",
        10: "If you built your own society, what is the first rule you’re going to put in place?",
        11: "How would you describe your time in college in 3 words?",
        12: "Would you rather never be able to express yourself accurately or always have to say the exact truth?",
        13: "What is the funniest prank played on you or played by you?",
        14: "What is your favorite lifehack?",
        15: "Describe your personality using ice cream flavors",
        16: "If you could have a custom robot, what are the top 3 things that robot would do for you?",
        17: "What’s a hobby you always wanted to learn, but never picked up? And what stopped you?",
        18: "How did you meet your best friend?",
        19: "What's the worse thing you did as a kid?",
        20: "What has been your favorite project or task at MC or any other company you worked for?",
        21: "If you could choose a  company that we share the office space with, which company would it be?",
        22: "What's one thing you believed as a kid but is not real?",
        23: "What's one pet peeve you have that no one knows about?",
        24: "If you could build a house made out of untraditional materials, what would you make it from (ex: marshmellow, vegetables, plastic bags)?"
        25: "What commercial song always get stuck in your head?"
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
