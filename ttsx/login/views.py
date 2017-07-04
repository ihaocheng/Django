from django.shortcuts import render
from
# Create your views here.

def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')