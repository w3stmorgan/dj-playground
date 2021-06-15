from django.urls import path

from . import views

app_name = "website"

urlpatterns = [
    path("", views.index, name="index"),
    path("samples/", views.samples, name="samples"),
    path("temp-twilio", views.temp_twilio),
]
