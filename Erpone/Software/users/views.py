from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def home(request):
    print(request.POST)
 
    return render(request,'users/home.html')