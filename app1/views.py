from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request , message):
    return HttpResponse(f"<h1>{message}</h2>")
