from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from home.models import *
from django.contrib import messages

# Create your views here.

def home(request):

    return render(request, "home/home.html")


def reservacion(request):

    return render(request, "home/reservacion.html")

def faqs(request):

    return render(request, "home/faqs.html")

def contacto(request):

    return render(request, "home/contacto.html")

def albercas(request):

    return render(request, "home/albercas.html")

def areas(request):

    return render(request, "home/areas_naturales.html")