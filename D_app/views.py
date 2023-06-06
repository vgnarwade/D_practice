from django.shortcuts import render

# Create your views here.from

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World !!!")
