from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
import json

def index(request):
    return HttpResponse("Hello World! CHAD")

def chad(request):  
    print(json.loads(request.body))
    from_postman = request.POST.get('to_calculate')
    jsonDict = {
        'to_calculate': from_postman,
    }
    return JsonResponse(jsonDict)
