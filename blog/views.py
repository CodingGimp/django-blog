from django.shortcuts import render
from django.http import HttpResponse 

# Create views here.
def home(request):
    return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return HttpResponse('<h1>About Me</h1>')