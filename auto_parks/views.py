from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from auto_parks.models import AutoParkModel
from auto_parks.Serializer import AutoParkSerializer
from rest_framework.response import Response
from rest_framework import status

class AutoParkListCreateView(ListCreateAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer

class AutoParkRetrieveUpdateDestroyView(GenericAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer

    def get(self, *args, **kwargs):
        autopark = self.get_object()
        serializer = self.serializer_class(autopark)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        data = self.request.data
        autopark = self.get_object()
        serializer = self.get_serializer(autopark, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        data = self.request.data
        autopark = self.get_object()
        serializer = self.get_serializer(autopark, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



