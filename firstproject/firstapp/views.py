from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def text(request):
    return HttpResponse("Hello world! This is my first application")
