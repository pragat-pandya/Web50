from django.contrib.auth.models import AbstractUser
from django.db import models



class Listing(models.Model):
    id = models.AutoField(primary_key=True, )
    title = models.CharField(max_length=64, null=False)
    description = models.CharField(max_length=200, null=False)
    bid_init = models.IntegerField(null=False)
    img = models.URLField(null=True)
    curr_price = models.IntegerField(blank=True)

    def get (self,arg):
        return self.arg
    
    def __str__ (self):
        return f"{self.id} : {self.title} : {self.description} : {self.bid_init} : {self.img}"


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    listings = models.ManyToManyField(Listing, blank=True, related_name="user_listings")


class bids (models.Model):
    bID = models.AutoField(primary_key=True)
    lid = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    bid_amount = models.IntegerField(null=False)

class comments (models.Model):
    cid = models.AutoField(primary_key=True)
    lid = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    cbody = models.CharField(max_length=100, null=False)

class watchlist (models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=100)
    item = models.ManyToManyField (Listing, related_name="listing")