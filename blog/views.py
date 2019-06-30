from django.shortcuts import render
from django.http import HttpResponse 

# Create views here.
def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return HttpResponse('<h1>About Me</h1>')