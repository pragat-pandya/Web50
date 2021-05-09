from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *
from .forms import ListingForm 
from django.contrib.auth.decorators import login_required




def index(request):
    listings = Listing.objects.all()
    return render(request, "auctions/index.html", {
        "message" : list(listings)
    })


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


def listing_page (request, listing_title):
    obj = Listing.objects.get(title=listing_title)
    #try:
    owner = False
    if request.user == obj.owner:
        owner = True
    
    try:
        flag = request.user.watcher.filter(item=obj).exists()
    except AttributeError:
        flag = False
    bids = obj.bids.all()
    return render (request, "auctions/listing_page.html", {
        "flag" : flag,
        "listing" : obj,
        "title" : listing_title,
        "image" : obj.img,
        "price" : obj.curr_price,
        "description" : obj.description,
        "initial_bid" : obj.bid_init,
        "bid_validity" : True,
        "prev_bids" : obj.bids.all().exists(), 
        "bids" :  obj.bids.all(),
        "owner" : owner,
        "isclosed" : False,
        "iscomments" : Comment.objects.filter(item = obj).exists(),
        "comments" : Comment.objects.filter(item=obj),
    })


# Add new listing to the app
@login_required(login_url='/login', redirect_field_name='index')
def add_listing (request):
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
            listing.curr_price = listing.bid_init
            listing.owner = User.objects.get(username=new_listing.cleaned_data["ownr"])
            # Append this record to the Listing table.
            listing.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            # If the form is not valid then redirect to add_listing.html with invalid message.
            render (request, "auctions/add_listing.html", {
                "message" : "The data submitted is not valid!",
                "form" : ListingForm()
            })
    
    return render(request, "auctions/add_listing.html", {
        "message": None,
        "form" : ListingForm()
    })

@login_required(login_url='/login', redirect_field_name='index')
def watch (request):
    if request.method == "POST":
        # Create a new object of wl containing current user and choosed listing item.
        wl = Watchlist(item=Listing.objects.get(title=request.POST["title"]), usr=request.user)
        # Save it to the database.
        wl.save()
        # Redirect the user to that same listing page.
        return HttpResponseRedirect(reverse("listing_page", kwargs={'listing_title': request.POST["title"]}))
    # On get request go to index.
    return render(request, "auctions/index.html", {
        "message" : list(Listings.objects.all())
    })

@login_required(login_url='/login', redirect_field_name='index')
def unwatch (request):
    if request.method == "POST":
        # Get the watchlist object from the database.
        wl = Watchlist.objects.get(item=Listing.objects.get(title=request.POST["title"]), usr=request.user)
        # Delete this record from database.
        wl.delete()
        # Redirect the user to the same listing page.
        return HttpResponseRedirect(reverse("listing_page", kwargs={'listing_title': request.POST["title"]}))
    # On get request go to index
    return render (request, "auctions/index.html", {
        "message" : list(Listings.objects.all())
    })


@login_required(login_url='/login', redirect_field_name='index')
def watchlist (request):
    listings = Watchlist.objects.filter(usr = request.user)
    if listings.exists():
        items = listings
        return render(request, "auctions/watchlist.html", {
            "message" : items,
            "flag" : True,
        })
    else:
        return render(request, "auctions/watchlist.html", {
            "flag" : False
        })    

@login_required(login_url='/login', redirect_field_name='index')
def make_a_bid (request):
    # If its a post request it is a bid makking scenario
    if request.method == "POST":
        # Get the listing object in question of bid
        l = Listing.objects.get(title=request.POST["title"])
        # Check if the bid is valid 
        if int(request.POST["bid_amount"]) > l.curr_price and l.owner != request.user:
            l.curr_price = int(request.POST["bid_amount"])
            # Make these changes to table row
            l.save()
            # Populate a Bid object!
            b = Bid()
            b.item = l
            b.amount = request.POST["bid_amount"]
            b.usr = request.user
            # Save this new bid 
            b.save()
            return render (request, "auctions/listing_page.html", {
                "flag" : request.user.watcher.filter(item=l).exists(),
                "listing" : l,
                "title" : l.title,
                "image" : l.img,
                "price" : l.curr_price,
                "description" : l.description,
                "initial_bid" : l.bid_init,
                "bid_validity" : True,
                "prev_bids" : l.bids.all().exists(),
                "bids" : l.bids.all(),
                "owner" : request.user == l.owner,
                "isclosed": False,
                "iscomments" : Comment.objects.filter(item = obj).exists(),
                "comments" : Comment.objects.filter(item=obj),
            })
        else:
            return render (request, "auctions/listing_page.html", {
                "flag" : request.user.watcher.filter(item=l).exists(),
                "listing" : l,
                "title" : l.title,
                "image" : l.img,
                "price" : l.curr_price,
                "description" : l.description,
                "initial_bid" : l.bid_init,
                "bid_validity" : False,
                "prev_bids" : l.bids.all().exists(),
                "bids" :  l.bids.all(),
                "owner" : request.user == l.owner,
                "isclosed": False,
                "iscomments" : Comment.objects.filter(item = obj).exists(),
                "comments" : Comment.objects.filter(item=obj),
            })

@login_required(login_url='/login', redirect_field_name='index')
def close (request):
    if request.method == "POST":
        # The item which is closing
        l = Listing.objects.get(title=request.POST["title"])
        # Winning bid who owned the item
        winning_bid = Bid.objects.get(item=l,amount=l.curr_price)
        # The user who made that bid
        winner = winning_bid.usr
        return render (request, "auctions/listing_page.html", {
                "flag" : request.user.watcher.filter(item=l).exists(),
                "listing" : l,
                "title" : l.title,
                "image" : l.img,
                "price" : l.curr_price,
                "description" : l.description,
                "initial_bid" : l.bid_init,
                "bid_validity" : False,
                "prev_bids" : l.bids.all().exists(),
                "bids" :  l.bids.all(),
                "owner" : request.user == l.owner,
                "isclosed": True,
                "winner" : winner,
                "iscomments" : Comment.objects.filter(item = obj).exists(),
                "comments" : Comment.objects.filter(item=obj),
            })  

@login_required(login_url='/login', redirect_field_name='index')
def add_comment(request):
    if request.method == "POST":
        c = Comment()
        c.body = request.POST["cbody"]
        c.item = Listing.objects.get(title=request.POST.get('item-name'))
        c.usr = request.user
        c.save()    
        return HttpResponseRedirect(reverse("listing_page", kwargs={'listing_title': request.POST.get('item-name')}))
