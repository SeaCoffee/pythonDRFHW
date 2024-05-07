from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDestroyView, UserAutoParksListView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-profile'),
    path('users/<int:user_id>/autoparks/', UserAutoParksListView.as_view(), name='user-autoparks-list'),
]