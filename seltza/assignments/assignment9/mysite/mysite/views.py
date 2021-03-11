from django.shortcuts import render
from django.http import HttpResponse
import json


def calc(obj, expr='4 + 5'):
    print(expr)
    ans = obj.calculate(expr)
    if ans:
        print(ans)

def index(request):
    return HttpResponse("Hello, world. You're at deez.")

def calc(request):
    to_calc = request.POST.get('to_calculate')
    c = Calculator(throw=False)
    ans = calc(c, to_calc)
    resp = { 'ans' : str(ans)}
    return JsonResponse(resp)