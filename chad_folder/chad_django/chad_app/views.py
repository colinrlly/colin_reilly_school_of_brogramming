from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World! CHAD")

def chad(request):
    return HttpResponse("WOAH CHAD!")
