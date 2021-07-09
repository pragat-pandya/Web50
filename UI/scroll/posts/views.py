import time
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, "posts/index.html")

def posts (request):
    # Get start and end points 
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start+9))

    # Genarate list of posts
    data = []
    for i in range (start, end+1):
        data.append(f"Post #{i}")
    
    # Artificially delay speed of the response
    time.sleep(1)

    # Return list of posts as a Json object
    # JsonResponse takes python dictionary as argumnet.
    return JsonResponse ({
        "posts": data
    })