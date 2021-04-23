from django.shortcuts import render
from .models import Flight, Passengers
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import urls

def index(request):
    return render(request, 'flights/index.html', {
         'AllFlights' : Flight.objects.all()
     })


def single(request, flightID):
     if Flight.objects.count() < flightID:
          return HttpResponse('Flight ID was not found :(')

     fli = Flight.objects.get(id = flightID)
     return render(request, 'flights/single.html', {
          'fli': fli,
          'AllPass': fli.passengers.all(),
          'NonPass': Passengers.objects.exclude(flights = fli).all()
     })


def book(request, flightID):
     if request.method == 'POST':
          fli = Flight.objects.get(id = flightID)
          pas = Passengers.objects.get(id = int(request.POST['passenger']))
          pas.flights.add(fli)
          return HttpResponseRedirect(reverse('flights:single', args = (fli.id, )))