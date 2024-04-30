from rest_framework.views import APIView
from rest_framework.response import Response
from cars.models import CarModel
from .serializers import CarSerializer, CarListSerializer
from rest_framework import status



class CarListCreateView(APIView):
    def get(self, request, *args, **kwargs):
        cars = CarModel.objects.all()
        serializer = CarListSerializer(cars, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarRetrieveUpdateDestroyView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response('Cars not found', status=status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response('Cars not found', status=status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, *args, **kwargs):
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response('Cars not found', status=status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







