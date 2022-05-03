from django.shortcuts import render
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Car
from .serializers import CarSerializer, PostCarSerializer

class GetAllCars(APIView):
    def get(self, request):
        list_car = Car.objects.all()
        mydata = CarSerializer(list_car, many=True)
        return Response(data=mydata.data, status=status.HTTP_200_OK)

    def post(self, request):
        mydata = PostCarSerializer(data=request.data)
        if not mydata.is_valid():
            return Response('sai du lieu roi', status=status.HTTP_400_BAD_REQUEST)
        name = mydata.data['name']
        color = mydata.data['color']
        brand = mydata.data['brand']
        #mydata.save()
        c = Car.objects.create(name=name, color=color, brand=brand)
        return Response(data=c.name, status=status.HTTP_200_OK)

