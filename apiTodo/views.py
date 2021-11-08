from django.http.response import HttpResponse
from django.shortcuts import render
from .serializers import TodoSerializer
from .models import Todo

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

def home (request):
  return HttpResponse('<center><h1 style="background-color:powderblue;">KHAN DRF Funtional View Page</h1><center>')


@api_view()
def TodoList(request):
  querset = Todo.objects.all()
  
  serializer = TodoSerializer(querset, many=True)
  
  return Response (serializer.data)
  
  