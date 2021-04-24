from django.contrib.auth.models import AbstractUser
from django.db import models



class Listing(models.Model):
    id = models.AutoField(primary_key=True, )
    title = models.CharField(max_length=64, null=False)
    description = models.CharField(max_length=500, null=False)
    bid_init = models.IntegerField(null=False)
    img = models.URLField(null=True)
    
    def __str__ (self):
        return f"{self.id} : {self.title} : {self.description} : {self.bid_init} : {self.img}"

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    listings = models.ManyToManyField(Listing, blank=True, related_name="user_listings")
