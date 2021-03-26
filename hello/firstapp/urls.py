from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("hackerspace", views.hackerspace, name = "hackerspace"),
    path("<str:name>", views.greet, name = "greet")
]
