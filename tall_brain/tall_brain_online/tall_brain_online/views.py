from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from .helper.TallCalc import tallCalc
from .models import CalculateHistory

# Create your views here.
def index(request):
    return HttpResponse("Hello, brofessor! Please proceed to fugma.")

def calculate(request):

    print(json.loads(request.body))

    returnDict = {}

    problem = json.loads(request.body)
    
    returnDict['calculated'] = tCalc.calculate(problem['to_calculate'])
    
    print(returnDict['calculated'])

    row = CalculateHistory(problem=problem['to_calculate'], solution=returnDict['calculated'])
    row.save()

    if request.method == 'POST':
        return JsonResponse(returnDict)

    

tCalc = tallCalc()
