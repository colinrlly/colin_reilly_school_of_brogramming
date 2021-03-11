from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
import json

from chad_django.models import CalculateHistory

def index(request):
    return HttpResponse("Hello World! CHAD")

def chad(request):  
    body = json.loads(request.body)

    print(body)

    row = CalculateHistory(input=body['to_calculate'], output='9')
    row.save()

    return JsonResponse(body)
