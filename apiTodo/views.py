from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def home (request):
  return HttpResponse('<center><h1 style="background-color:powderblue;">KHAN DRF Funtional View Page</h1><center>')