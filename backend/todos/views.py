from django.shortcuts import render
from rest_framework import generics
from . import models
from .serializers import TodoSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Create your views here.
#api/todos/
#class ListTodo(APIView):
    
    # def get(self, request): #request to list all items in Todos
    #     todo = Todos.objects.all()
    #     serializer = TodoSerializer(todo, many=True)
    #     return Response(serializer.data)
        
    # def post(self): #creates new item
    #     pass
    

class ListTodo(generics.ListCreateAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer
    
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer
    
    
    # def get_queryset(self):
    #     return Todos.objects.all().filter(user=self.request.user)