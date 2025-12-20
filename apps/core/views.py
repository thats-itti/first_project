from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.generics import ListAPIView , CreateAPIView , UpdateAPIView , DestroyAPIView , RetrieveAPIView , ListCreateAPIView
from .models import Todos , Todos_history , Records , Dailytodos,User
from .serializer import Daily_serializer , Todos_history_serializer , Todos_serializer , Recods_serializers
from rest_framework import status
from datetime import datetime
from django.core.exceptions import ValidationError
# from django import status
# Create your views here.

class Todos_otherview(
                     DestroyAPIView,
                     RetrieveAPIView,
                     UpdateAPIView,
                     CreateAPIView,
                     ):
    # def dispatch(self, request, *args, **kwargs):
    #     if 'pk'  not in kwargs and request.method in ['PATCH','PUT','DELETE']:
    #         return Response({"details":"method not allowed without pk "},status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #     return super().dispatch(request, *args, **kwargs)

    serializer_class = Todos_serializer 
    lookup_field = "pk"
    def get_queryset(self):
        qs = Todos.objects.all().filter(id = self.kwargs.get('pk')).filter(is_active=True)
        return qs
    def perform_destroy(self, instance):
        instance.is_active = False
        Dailytodos.objects.all().filter(link=instance).update(is_active=False)
        Todos_history.objects.all().filter(todo=instance).update(is_active=False)
        instance.save()
        
    def perform_create(self, serializer):
        serializer.save(user= self.request.user)
    
class Todo_listview(ListCreateAPIView):
    serializer_class = Todos_serializer
    def get_queryset(self):
        qs = Todos.objects.all().filter(is_active=True)
        return qs
     
    def perform_create(self, serializer):
        serializer.save(user= self.request.user)   

class DailyTodo_view(
                     CreateAPIView,
                     RetrieveAPIView,
                     DestroyAPIView,
                     UpdateAPIView,
                     ):
    serializer_class = Daily_serializer
    def get_queryset(self):
        if self.kwargs.get('pk') is not None:
            qs = Dailytodos.objects.all().filter(id = self.kwargs.get('pk')).filter(is_active=True)
        else:
            qs = Dailytodos.objects.all().filter(is_active=True)
        return qs
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

class DailyTodo_view1(
                     ListCreateAPIView
                     ):
    serializer_class = Daily_serializer
    def get_queryset(self):
        qs = Dailytodos.objects.all().filter(is_active=True)
        return qs
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class RecordTodo_view(
                     CreateAPIView,
                     RetrieveAPIView,
                     DestroyAPIView,
                     UpdateAPIView,
                     ):
    serializer_class = Recods_serializers
    def get_queryset(self):
        qs = Records.objects.all().filter(id = self.kwargs.get('pk')).filter(is_active=True)
        return qs
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

class RecordTodo_view1(ListAPIView,
                     CreateAPIView,
                     ):
    serializer_class = Recods_serializers
    def get_queryset(self):
        qs = Records.objects.all().filter(is_active=True)
        return qs
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    

class TodoHistory_view(
                     CreateAPIView,
                     RetrieveAPIView,
                     DestroyAPIView,
                     UpdateAPIView,
                     ):
    serializer_class = Todos_history_serializer
    def get_queryset(self):
        qs = Todos_history.objects.all().filter(id = self.kwargs.get('pk')).filter(is_active=True)        
        return qs
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

class TodoHistory_view1(ListAPIView,
                     CreateAPIView,
                     ):
    serializer_class = Todos_history_serializer
    def get_queryset(self):
        qs = Todos_history.objects.all().filter(is_active=True)
        return qs
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


























    # def update(self, request, *args, **kwargs):
    #     qs = self.get_queryset()
    #     serializer = self.get_serializer(qs,data=request.data,partial=True)
    #     serializer.is_valid(raise_exceptions=True)
    #     serializer.save()
    #     return super().update(request, *args, **kwargs)
    # def perform_update(self, serializer):


    #     return super().perform_update(serializer)

# class Todos_destroyapiview(DestroyAPIView):
#     queryset = Todos.objects.all()
#     lookup_field = 'pk'

# class Todos_createapiview(ListCreateAPIView):
#     queryset = Todos.objects.all()
#     serializer_class = Todos_serializer
#     lookup_field = "pk"

#     def get(self,request,*args,**kwargs):
#         return super().get(request,*args,**kwargs)
    
#     def get_queryset(self):
#         print("hello world")
#         print(self)
#         return super().get_queryset()

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

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