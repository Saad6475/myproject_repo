from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Hi i am Saad</h1><h3>Hello this website is uploaded on Heroku </h3>')