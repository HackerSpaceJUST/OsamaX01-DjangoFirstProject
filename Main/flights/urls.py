from django.urls import path

from . import views

app_name = 'flights'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:flightID>', views.single, name = "single"),
    path('<int:flightID>/book', views.book, name = "book"),
] 