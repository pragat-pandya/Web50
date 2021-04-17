from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index (request):
  return HttpResponse("<h1 style=\"color: blue;\">Hello, World!</h1>")

def pragat (request):
  return HttpResponse("Hello, Pragat!")

def brian (request):
  return HttpResponse("Hello, Brian!")

def david (request):
  return HttpResponse("Hello, David!")