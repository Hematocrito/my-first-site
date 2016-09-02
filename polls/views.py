from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Mi corazón soporta el peso abrumador de sus rigores. Romeo y Julieta.-")