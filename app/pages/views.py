from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    """index page for pages view"""
    return render(request, 'pages/index.html')


def about(request):
    """Shows about page"""
    return render(request, 'pages/about.html')