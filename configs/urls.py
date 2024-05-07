from django.urls import path
from django.urls import path, include


urlpatterns = [
    path('cars', include('cars.urls')),
]