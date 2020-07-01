from django.test import TestCase
from offsite_questions.models import Entry

# Create your tests here.

class EntryTest(TestCase):

    def test_total_count_behaves_correctly(self):
        #Ensure total count behaves accurately 
        initial_count = Entry.total_count()
        self.assertEquals(0, initial_count)

        # Let's create some entries
        Entry(question_number = 1, question_text = "Testing question 1").save()
        Entry(question_number = 2, question_text = "Testing question 2").save()
        Entry(question_number = 3, question_text = "Testing question 3").save()
        
        new_count = Entry.total_count()
        self.assertEquals(3, new_count)
        pass


    def test_error_when_exceed_max_index(self):    
        #User receives error message if they input a number that's beyond the index

         # Let's create some more entries
        Entry(question_number = 1, question_text = "Testing question 1").save()
        Entry(question_number = 2, question_text = "Testing question 2").save()
        Entry(question_number = 3, question_text = "Testing question 3").save()

        self.assertRaises(Entry.DoesNotExist, Entry.objects.get, question_number=4)
        pass


if __name__ == '__main__':
    TestCase.main()







