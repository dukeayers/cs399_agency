from django.db import models

# Create your models here.

class Location(models.Model):
	zip = models.IntegerField(max_length = 5)
	city = models.CharField(max_length = 100)
	state = models.CharField(max_length = 2)
	street = models.CharField(max_length = 200)

class CustomerInfo(models.Model):
	online = 'ON'
	radio = 'RA'
	friend = 'FR'
	search = 'SE'
	social = 'SO'
	
	referenceChoices = (
		(online, 'Online'),
		(radio, 'Radio'),
		(friend, 'Friend'),
		(search, 'Search Engine'),
		(social, 'Social Media'),
	)
	
	firstName = models.CharField(max_length = 32)
	lastName = models.CharField(max_length = 32)
	email = models.EmailField(label='E-mail')
	reference = models.CharField(max_length = 2, choices = referenceChoices, default = null)