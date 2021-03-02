from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hewo uwu, world-chan is kawaii desu.")
    