import json

from empress_django_project.models import CalculateHistory
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .helper.calculator import Calculator

def index(request):
    return HttpResponse("Hewo uwu, world-chan is kawaii desu.")

def calculate(request):
    data = {}

    # set variable that accepts postman request body "'to_calculate': '4+5'"
    # and parse's that body - string --> json object.
    var = json.loads(request.body)
    
    calc = Calculator()
    result = calc.calculate(var["to_calculate"])
    
    data["ans"] = result

    print(data["ans"])

    row = CalculateHistory(input = var["to_calculate"], result = data["ans"])
    row.save()

    if request.method == 'POST':
        return JsonResponse(data)
