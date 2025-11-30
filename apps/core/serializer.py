from rest_framework import serializers
from .models import Login , records , dailytodos , Todos

class recods_serializers(serializers.ModelSerializer):


    class Meta:
        Model  =records 
        field = [
            'task',
            'description',
            'issued_date'
        ]

class Todos_serializer(serializers.Modelserializer):
     
    class Meta:
        Model = Todos
        field = [
            'task',
            'description',
            'completed',
            'completed_time',
            'total_time',
            'issued_date',
            
        ]

class Daily_serializer(serializers.ModelSerializer):


    class Meta:
        Model = dailytodos 
        field = [
            'task',
            'description',
            'completed_time',
            'completed',
            'completed_time',
            'daily_time',
            
        ]