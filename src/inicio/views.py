from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def miHomeView(*args, **kwargs):
    return HttpResponse("<h1> Mi primera vista </h1>")

def otraVista(*args, **kwargs):
    return HttpResponse("<h1> Mi otra vista </h1>")