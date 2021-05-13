import json

from empress_django_project.models import CalculateHistory
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .helper.calculator import Calculator

def index(request):
    pee = request.GET.get('calculator_input', None)

    if pee :
        calc = Calculator() 
        result = calc.calculate(pee)
        
        return render(request, 'index.html', {'result': result})

    else:
        return render(request, 'index.html')
