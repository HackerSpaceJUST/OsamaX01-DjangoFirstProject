from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('hackerspace', views.Hackerspace, name = "hackerspace"),
    path('<str:name>', views.GeneralName, name = "GeneralName"),
]

