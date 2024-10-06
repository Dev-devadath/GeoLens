from django.urls import path
from . import views

app_name = "geolens"
urlpatterns = [
    path("", views.index, name="index"),
    path('api/get-soil-data/', views.get_soil_data, name='get_soil_data'),
]
