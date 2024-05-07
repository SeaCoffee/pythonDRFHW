from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response
from models import UsersModel
from serializers_users import UsersSerializer
from auto_parks.Serializer import AutoParkSerializer

class UserListCreateView(ListCreateAPIView):
    queryset = UsersModel.objects.all()
    serializer_class = UsersSerializer

class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = UsersModel.objects.all()
    serializer_class = UsersSerializer

class UserAutoParksListView(ListAPIView):
    serializer_class = AutoParkSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        user = UsersModel.objects.get(id=user_id)
        return user.autoparks.all()
