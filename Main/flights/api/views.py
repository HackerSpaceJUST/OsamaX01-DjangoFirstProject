from django.shortcuts import render

from rest_framework import viewsets, permissions

from flights.models import Flight, Airport, Passengers
from .serializers import FlightSerializer, AirportSerializer, PassengersSerializer

class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes_by_action = {
        'create': [permissions.IsAdminUser],
        'list': [permissions.IsAuthenticatedOrReadOnly],
        'update': [permissions.IsAdminUser],
        'destroy': [permissions.IsAdminUser],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

class AirportView(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    permission_classes_by_action = {
        'create': [permissions.IsAdminUser],
        'list': [permissions.IsAuthenticatedOrReadOnly],
        'update': [permissions.IsAdminUser],
        'destroy': [permissions.IsAdminUser],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
    

class PassengerView(viewsets.ModelViewSet):
    queryset = Passengers.objects.all()
    serializer_class = PassengersSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
