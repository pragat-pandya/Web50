from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index (request):
  return render (request, "hello/index.html")

# Well following three functions allows us to greet three different persons 
# How about greeting 300 people ?? :: There's no point in defining 300 more views
#
#def pragat (request):
#  return HttpResponse("Hello, Pragat!")
#def brian (request):
#  return HttpResponse("Hello, Brian!")
#def david (request):
#  return HttpResponse("Hello, David!")
#
#

# TO GET THE TASK DONE Let's create a new view which will use a url as it's parameter
def greet (request, name):
  return render (request, "hello/greet.html", {
    "name" : name.capitalize()
  })