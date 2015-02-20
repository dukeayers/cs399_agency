from django.db import models
from django.forms import ModelForm
from django import forms
from localflavor.us.forms import USStateSelect
from localflavor.us.forms import USZipCodeField
from localflavor.us.forms import USPhoneNumberField
import random

class Location(models.Model):
    street = models.CharField(max_length = 200)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 2)
    zip = models.IntegerField(max_length = 10)
    
class LocationForm(ModelForm):
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control altered-cookie', 'required': 'required', 'placeholder': 'City'}))
    state = forms.CharField(widget=USStateSelect(attrs={'class':'dropdown', 'required': 'required'}))
    zip = USZipCodeField(widget=forms.TextInput(attrs={'class': 'form-control altered-cookie', 'required': 'required', 'placeholder': 'Zip Code'}))
    street = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control altered-cookie', 'required': 'required', 'placeholder': 'Street Address'}))
    class Meta:
        model = Location

class Gerbil(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 12)
    gerbil_name = models.CharField(max_length = 200)
    street = models.CharField(max_length = 200)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 2)
    zip = models.IntegerField(max_length = 10)
    
class GerbilForm(ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control altered-cookie', 'required': 'required', 'placeholder': 'Your First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control altered-cookie', 'required': 'required', 'placeholder': 'Your Last Name'}))
    phone = USPhoneNumberField(widget=forms.TextInput(attrs={'class': 'form-control altered-cookie', 'required': 'required', 'placeholder': 'Your Phone Number'}))
    gerbil_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control altered-cookie', 'placeholder': 'Name the gerbil!'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control altered-cookie', 'required': 'required', 'placeholder': 'City'}))
    state = forms.CharField(widget=USStateSelect(attrs={'class':'dropdown', 'required': 'required'}))
    zip = USZipCodeField(widget=forms.TextInput(attrs={'class': 'form-control altered-cookie', 'required': 'required', 'placeholder': 'Zip Code'}))
    street = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control altered-cookie', 'required': 'required', 'placeholder': 'Street Address'}))
    class Meta:
        model = Gerbil
    
class Campaign(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    BeginDate = models.DateField()
    EndDate = models.DateField()

class Promo():
    promo= random.randrange(10000, 99999)