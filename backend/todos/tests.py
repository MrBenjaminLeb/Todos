from django.test import TestCase

# Create your tests here.
from .models import Todo   #import model to test  - for testing

# Create your tests here.

class TodosTest(TestCase):
    def create_todo(self, title="",description="instance with empty title"):    #add test case with empty title
        return Todo.objects.create(title=title, description=description)
        
    def test_todo_creation(self):
        new =   self.create_todo()
        self.assertEqual("",new.title)  #test whether test creation has an empty title