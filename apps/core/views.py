from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.generics import ListAPIView , CreateAPIView , UpdateAPIView , DestroyAPIView , RetrieveAPIView , ListCreateAPIView
from .models import Todos , Todos_history , Records , Dailytodos
from .serializer import Daily_serializer , Todos_history_serializer , Todos_serializer , Recods_serializers
from datetime import datetime
# from django import status
# Create your views here.



class Todos_listview(ListAPIView):
    queryset = Todos.objects.all() 
    serializer_class = Todos_serializer 
    lookup_field = "pk"



class Todos_createapiview(ListCreateAPIView):
    queryset = Todos.objects.all()
    serializer_class = Todos_serializer
    lookup_field = "pk"

    def get(self,request,*args,**kwargs):
        print(request.COOKIES)
        return super().get(self,request,*args,**kwargs)


    def create(self, request, *args, **kwargs):
        data = request.data
        data['user'] = request.user.id
       

        
        serializer = self.get_serializer(data=data)
        
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        serializer.save()
        print("hello workd")
        headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        response = Response(serializer.data)
        response.set_cookie("access","this is the token that could be used to login or so to do other acion so go on")
        return response

