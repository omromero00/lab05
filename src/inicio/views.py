from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def miHomeView(request, *args, **kwargs):
    print(request.user)
    micontexto={
        "mitexto": "hola texto",
        "minumero": 123,
    }
    return render(request, "home.html", micontexto)

def otraVista(*args, **kwargs):
    return HttpResponse("<h1> Mi otra vista </h1>")