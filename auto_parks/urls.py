from django.urls import path, include
from .views import AutoParkListCreateView, AutoParkRetrieveUpdateDestroyView


urlpatterns = [
    path('', AutoParkListCreateView.as_view(), name='auto_park_list'),
    path('autoparks/<int:pk>', AutoParkRetrieveUpdateDestroyView.as_view(), name='autoparks_retrieve_update_delete'),
]