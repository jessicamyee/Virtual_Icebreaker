from django.db import models
import random

# Create your models here.

class Entry (models.Model):
    """Entry of a hotsprings question"""
    question_number = models.IntegerField()
    question_text = models.CharField(max_length=200)

    def __str__(self):
        """Return a string representation of the model."""
        return str(self.question_text)
    
    @staticmethod
    def total_count():
        """Returns the total number of entries available."""
        return Entry.objects.all().count()

    @staticmethod
    def question_list():
        """Returns the list of questions."""
        return Entry.objects.all()

    @staticmethod
    def random_question():
        """Returns a random question."""
        return random.choice(Entry.question_list())

