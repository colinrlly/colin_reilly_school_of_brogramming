from django.shortcuts import render
from django.http import HttpResponse
import json
from .calculator import Calculator
from django.http import JsonResponse


def calc(obj, expr='4 + 5'):
    print(expr)
    ans = obj.calculate(expr)
    if ans:
        print(ans)

def index(request):
    return HttpResponse("Hello, world. You're at deez.")

def calculate(request):
    bdy = str(request.body)
    if bdy:
        parsed = json.loads(request.body)
        to_calc = parsed['to_calculate']
        c = Calculator(throw=False)
        calc(c, to_calc)
        ans = c.calculate(to_calc)
        resp = { 'ans' : str(ans)}
        return JsonResponse(resp)