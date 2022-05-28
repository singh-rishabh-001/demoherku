from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse   # added

def home(request):
    return HttpResponse('This is the home page.')