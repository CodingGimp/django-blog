from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Mario Gimp',
        'title': 'First post',
        'content': 'Content of the first post',
        'date_posted': 'July 1, 2019'
    },
    {
        'author': 'Imran Majid',
        'title': 'Second post',
        'content': 'Content of the second post',
        'date_posted': 'July 2, 2019'
    }
]    

# Create views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')