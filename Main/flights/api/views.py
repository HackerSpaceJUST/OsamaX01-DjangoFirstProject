from django.shortcuts import render

from rest_framework import viewsets

from flights.models import Flight, Airport, Passengers
from .serializers import FlightSerializer, AirportSerializer, PassengersSerializer

class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class AirportView(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer

class PassengerView(viewsets.ModelViewSet):
    queryset = Passengers.objects.all()
    serializer_class = PassengersSerializer
