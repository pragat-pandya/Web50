from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index (request):
  return HttpResponse("Hello, World!")

def pragat (request):
  return HttpResponse("Hello, Pragat!")

def brian (request):
  return HttpResponse("Hello, Brian!")

def david (request):
  return HttpResponse("Hello, David!")