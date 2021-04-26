from rest_framework import serializers

from flights.models import Flight, Airport, Passengers

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ('origin', 'destination', 'duration')

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ['code', 'city']
    
class PassengersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passengers
        fields = ['first', 'last', 'flights']