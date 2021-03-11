from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
import json

def index(request):
    return HttpResponse("Hello World! CHAD")

def chad(request):  
    print(json.loads(request.body))
    return JsonResponse(request.body)
