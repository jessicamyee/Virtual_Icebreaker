# Icebreaker-Generator

The primary purpose of this icebreaker generator (also known as the Hotsprings App) is to randomly generate questions teams can use as part of their icebreaker activity upon a click of a button.

## Motivation

2 big motivators: 
1. As many companies have switched to remote work due to COVID-19, team-specific and general meetings can be another source of "Zoom fatigue". Why not make these meetings more fun with an individualized and customized icebreaker question generator? Each person in the meeting would just enter the website and receive their own random icebreaker question to think about. 
2. Icebreaker activities can be stressful - especially for introverts. The reason this is called the Hotsprings App is to encourage team members (both introverts and extroverts) to ease into the conversation rather than forcefully "breaking the ice".


## Features
1. Public access to the standard 25 questions.
2. If desired, you can create a team on the website, modify the standard list of questions (removing and/or adding new questions) and the list of questions will only be viewable to those in your team. (feature still in progress)


## Installation

Install Python 3.6, pip (if not already pre-installed), and Django to start project

```bash
sudo apt-get update
sudo apt-get install python3.6
```

```bash
sudo python3 get-pip.py
```

```bash
sudo pip install Django==2.2.12
```

## Database

Uses SQLite. To install database:

```bash
python3 manage.py migrate
```

## Launching the website

1. Activate your virtual environment
```bash
source [your virtual environment's name]/bin/activate
```

2. Run your server
```bash
python3 manage.py runserver
```

## Platform support

This project is currently supported on Linux. 

## Contributing
Pull requests are welcome. For changes, please open an issue first to discuss what you would like to change.
