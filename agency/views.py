from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from agency.models import LocationForm, Campaign,Promo
# Create your views here.


def lists(request):
    return render(request, 'lists.html')

def home(request):
    return render(request, 'index.html')

def thanks(request):
    return render(request, 'thanks.html',{'promo':Promo.promo})

def about(request):
    return render(request, 'about.html', {'campaigns': Campaign.objects.all()})

def campaign(request, question_id):
    if request.method == 'POST':
        form = LocationForm(request.POST)

        if(form.is_valid()):
            form.save(commit = True)
            return HttpResponseRedirect('../../thanks')
    else:
        form = LocationForm()
    return render(request, 'campaign.html', {'CurrentCampaign': Campaign.objects.filter(id = question_id), 'form': form})
    #return HttpResponse("You want to see %s." %question_id)

def location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)

        if(form.is_valid()):
            form.save(commit = True)
            return HttpResponseRedirect('/')
    else:
        form = LocationForm()

    return render(request, 'about.html', {'form': form})