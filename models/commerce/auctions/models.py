from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    # A primary key for user table
    id = models.AutoField(primary_key=True)


class Listing(models.Model):
    # PK
    id = models.AutoField(primary_key=True, )
    # Title of the listing
    title = models.CharField(max_length=64, null=False)
    # Text description of the listing
    description = models.CharField(max_length=200, null=False)
    # Initial bid for the listing
    bid_init = models.IntegerField(null=False)
    # IMG url for listing
    img = models.URLField(null=True)
    # Current price of the listing
    curr_price = models.IntegerField(blank=True)
    # The user who created/added this listing
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")

    def __str__ (self):
        return f"{self.id} : {self.title} : {self.description} : {self.bid_init} : {self.img}"

class Watchlist (models.Model):
    id = models.AutoField(primary_key=True)
    # The listing which is being watched
    item = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="watching")
    # The user who's watching this listing
    usr = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watcher")

    def __str__ (self):
        return f"{self.item} : {self.usr}"