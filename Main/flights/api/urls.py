from django.urls import path, include

from rest_framework import routers

from flights.api import views

router = routers.DefaultRouter()
router.register('flights', views.FlightView)
router.register('airports', views.AirportView)
router.register('Passengers', views.PassengerView)

urlpatterns = [
    path('', include(router.urls)),
]