from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User, Listing
from .forms import ListingForm 




def index(request):
    return render(request, "auctions/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


# Add new listing to the app
def add_listing (request):
    # Create an instace of ListingForm to pass to the template!
    new = ListingForm()
    if request.method == "POST":
        
        # Store post request data into a ListingForm type object
        new_listing = ListingForm (request.POST)
        
        # Check if the form is valid
        if new_listing.is_valid():
            # If it's valid then use cleaned data to create a listing record
            listing = Listing ()
            listing.title = new_listing.cleaned_data["title"]
            listing.description = new_listing.cleaned_data["description"]
            listing.bid_init = new_listing.cleaned_data["initial_bid"]
            listing.img = new_listing.cleaned_data["img_url"]
            # Append this record to the db.
            listing.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            # If the form is not valid then redirect to add_listing.html with invalid message.
            render (request, "auctions/add_listing.html", {
                "message" : "The data submitted is not valid!",
                "form" : new
            })
    
    return render(request, "auctions/add_listing.html", {
        "message": None,
        "form" : new
    })