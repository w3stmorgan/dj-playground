from django.urls import path

from . import views

app_name = "airpollution"

urlpatterns = [
    path("upload/", views.upload, name="upload"),
    path("table/", views.table, name="table"),
    path("charts/", views.charts, name="charts"),
    path(
        "temp_country_creator", views.temp_country_creator, name="temp_country_creator"
    ),
]
