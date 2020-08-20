from django.db import models
import random

# Create your models here.

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    subdomain_prefix = models.CharField(max_length=100, unique=True)

class TenantAwareModel(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    class Meta:
        abstract = True    

class Entry (TenantAwareModel):
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

