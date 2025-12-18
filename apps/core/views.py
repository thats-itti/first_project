from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.generics import ListAPIView , CreateAPIView , UpdateAPIView , DestroyAPIView , RetrieveAPIView , ListCreateAPIView
from .models import Todos , Todos_history , Records , Dailytodos,User
from .serializer import Daily_serializer , Todos_history_serializer , Todos_serializer , Recods_serializers
from rest_framework import status
from datetime import datetime
# from django import status
# Create your views here.



class Todos_listview(ListAPIView):
    
    serializer_class = Todos_serializer 
    def get_queryset(self):
        qs = Todos.objects.all().filter(is_active=True)
        return qs
    def get(self, request, *args, **kwargs):
        qs = self.get_queryset()
        serializer = self.serializer_class(qs , many = True)
        return Response(serializer.data,status = status.HTTP_200_OK)


class Todos_destroyapiview(DestroyAPIView):
    queryset = Todos.objects.all()
    lookup_field = 'pk'
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Todos_createapiview(ListCreateAPIView):
    queryset = Todos.objects.all()
    serializer_class = Todos_serializer
    lookup_field = "pk"

    def get(self,request,*args,**kwargs):
        return super().get(request,*args,**kwargs)
 
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def create(self, request, *args, **kwargs):
    #     data = request.data
    #     serializer = self.get_serializer(data = request.data)

        # data = []
        # data['user'] = request.user.id
        # data += request.data
              
        # serializer = self.get_serializer(data = request.data)
        # if serializer.is_valid(raise_exception=True):
        #    self.perform_create(serializer)
           
    #    print(serializer)
    #    serializer["user"] = request.user.id

        # data = request.data
        # data['user'] = request.user.id
        # serializer = self.get_serializer(data = data)
        # if serializer.is_valid(raise_exception=True):
        #     self.perfom_create(serializer)
        # print(data)
        # serializer = self.get_serializer(data= data)
        # if serializer.is_valid(raise_exception=True):
        #     serializer.save()
        #     return Response(serializer.data,status= status.HTTP_201_CREATED)
 
        # data = request.data
        # data['user'] = request.user.id
        # serializer = self.get_serializer(data=data)
        # headers = self.get_success_headers(serializer.data)
        # print(headers)
        # if serializer.is_valid(raise_exception=True):
        #     serializer.save()
        #     return Response(serializer.data,status=status.HTTP_201_CREATED,headers=headers)
        # else:
        #     raise validationerror('ERROR FORM OF DATA')
        # # # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        # # response = Response(serializer.data)
        # # response.set_cookie("access","this is the token that could be used to login or so to do other acion so go on")

        # # return response
