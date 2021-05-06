from django import forms
from .models import Listing

class ListingForm(forms.Form):
  title = forms.CharField(label="Title", max_length=64, widget=forms.TextInput(attrs={'class':'form-control'}))
  description = forms.CharField(label="Description", widget=forms.Textarea(attrs={'class':'form-control'}), max_length=500)
  initial_bid = forms.IntegerField (label="Initial Bid($)", widget=forms.TextInput(attrs={'class': 'form-control'}))
  img_url = forms.URLField(label="Link to an image of the product", max_length=500, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
  ownr = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class':'form-control'}))