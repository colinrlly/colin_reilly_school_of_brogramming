from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json


# Create your views here.
def index(request):
    return HttpResponse("Hello, brofessor! Please proceed to fugma.")

def calculate(request):
    print(request.POST)
    testDict = {
        'data': request.POST.get('to_calculate', '')
    }
    return JsonResponse(testDict)