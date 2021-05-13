from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
import json

from chad_django.models import CalculateHistory

def index(request):
    calculator_input = request.GET.get('calculator_input', None)

    if calculator_input:
        row = CalculateHistory(input=calculator_input, output='9')
        row.save()

        return render(request, 'index.html', {'input': calculator_input})
    return render(request, 'index.html')
