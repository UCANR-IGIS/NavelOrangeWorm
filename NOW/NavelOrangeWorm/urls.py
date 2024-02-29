from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("events", views.events, name="events"),
    path("contact", views.contact, name="contact"),
    path("overview", views.overview, name="overview"),
    path("phenology", views.phenology, name="phenology"),
    path("resources", views.resources, name="resources"),
]