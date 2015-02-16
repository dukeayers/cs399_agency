from django.db import models
from django.forms import ModelForm
from django import forms
from localflavor.us.forms import USStateSelect
from localflavor.us.forms import USZipCodeField
# Create your models here.

class Location(models.Model):
    zip = models.IntegerField(max_length = 10)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 2)
    street = models.CharField(max_length = 200)

class LocationForm(ModelForm):
    zip = USZipCodeField(widget=forms.TextInput(attrs={'class': 'form-control altered-cookie', 'required': 'required', 'placeholder': 'Zip Code'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control altered-cookie', 'required': 'required', 'placeholder': 'City'}))
    state = forms.CharField(widget=USStateSelect(attrs={'class':'dropdown', 'required': 'required'}))
    street = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control altered-cookie', 'required': 'required', 'placeholder': 'Street Address'}))
    class Meta:
        model = Location

class Campaign(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    BeginDate = models.DateField()
    EndDate = models.DateField()

# class CustomerInfo(models.Model):
#     online = 'ON'
#     radio = 'RA'
#     friend = 'FR'
#     search = 'SE'
#     social = 'SO'
#     referenceChoices = (
#         (online, 'Online'),
#         (radio, 'Radio'),
#         (friend, 'Friend'),
#         (search, 'Search Engine'),
#         (social, 'Social Media'),
#     )
#     firstName = models.CharField(max_length = 32)
#     lastName = models.CharField(max_length = 32)
#     email = models.EmailField(label='E-mail')
#     #reference = models.CharField(max_length = 2, choices = referenceChoices, default = null)