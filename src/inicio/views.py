from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def miHomeView(request, *args, **kwargs):
    print(request.user)
    return render(request, "home.html", {})

def otraVista(*args, **kwargs):
    return HttpResponse("<h1> Mi otra vista </h1>")