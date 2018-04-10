from django.db import models

# Create your models here.
class Todo(models.Model):
    title   =   models.CharField(max_length=200) #title fieled defined with max length
    description =   models.TextField(max_length=1000) #titles field generated
    
    def __str__(self): #module to display title of object when retrieved
        return self.title