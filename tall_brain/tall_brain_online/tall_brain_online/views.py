from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect
from django.shortcuts    import render
from django.http         import HttpResponse
from django.http         import JsonResponse

import json

from .helper.TallCalc    import tallCalc
from .models             import CalculateHistory


def index(request):
    
    return render(request, 'index.html')


def calculate(request):

    prob = request.GET.get('calculator_input')

    if prob:

        row = CalculateHistory(problem=prob, solution=tCalc.calculate(prob))
        row.save()

        return render(request, 'calculate.html', {'result': tCalc.calculate(prob)})


    else:

        return render(request, 'calculate.html', {'result': 'Enter Numbers, Asshole'})


tCalc = tallCalc()
