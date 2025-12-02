from rest_framework import serializers
from .models import Login , records , dailytodos , Todos , Todos_history
from django.core.exceptions import ValidationError

class Recods_serializers(serializers.ModelSerializer):
    def __init__(self,*args,**kwargs):
        request = kwargs.get("context",{}).get("request") or None
        str_fields = request.GET.get("Records","") if request else None
        fields = str_fields.split(',') if str_fields else None
        super().__init__(*args,**kwargs)
        if fields  != None:
            allowed = set(fields)
            all_fields = set(self.fields)
            for field_name in all_fields - allowed:
                self.fields.pop(field_name)
            

    class Meta:
        model  =records 
        fields = [
            'task',
            'description',
            'issued_date'
            "task_date"
        ]
    

class Todos_serializer(serializers.Modelserializer):
    def __init__(self,*args,**kwargs):
        request = kwargs.get("context",{}).get("request") 
        str_fields = request.GET.get("Todos","") if request else None
        fields = str_fields.split(',') if str_fields else None
        super().__init__(*args,**kwargs)
        if fields  is not None:
            allowed = set(fields)
            all_fields = set(self.fields)
            for field_name in all_fields - allowed:
                self.fields.pop(field_name)
        
            
    
    class Meta:
        model = Todos
        fields = [
            'task',
            'description',
            'completed',
            'completed_time',
            'total_time',
            'issued_date',
            'task_date',
            'time_based',
            'daily_based',
            'daily_time',
            "remaining_time"
            
        ]
    def validate(self,data):
        if data.get("time_based"):
            if data.get("total_time") == "" or data.get("total_time") == "null":
               raise ValidationError("total time need to be insert for the time based task ") 
        if data.get("issued_date") < data.get("task_date"):
                raise ValidationError("task cannot be schedule for past date")
        if data.get("daily_based"):
            if data.get("daily_time") == "null" or data.get("daily_time") == "":
                raise ValidationError("daily time need to be assigned for daily based task")
        if data.get("comleted_time") != ("null" , "") and data.get("time_based"):
            if data.get('total_time') <= data.get('completed_time'):
                if not data.get("completed"):
                    data['completed'] = True
        return super().validate(data)


        
                
        

class Daily_serializer(serializers.ModelSerializer):

    def __init__(self,*args,**kwargs):
        request = kwargs.get("context",{}).get("request") 
        str_fields = request.GET.get("Dailytodos","") if request else None
        fields = str_fields.split(',') if str_fields else None
        super().__init__(*args,**kwargs)
        if fields  is not None:
            allowed = set(fields)
            all_fields = set(self.fields)
            for field_name in all_fields - allowed:
                self.fields.pop(field_name)
            

    class Meta:
        model = dailytodos 
        fields = [
            'task',
            'description',
            'completed_time',
            'completed',
            'daily_time',
            "time_based"
            
        ]
    def validate(self, data):
        if data.get('time_based'):
            if data.get("daily_time") == "none" or data.get('daily_time') == "":
                raise ValidationError("time need to be provided in time based task")
            if data.get('completed_time') in ('', 'null'):
                raise ValidationError("not time based cannot have completed time stored")
        return super().validate(data)
         
class Todos_history_serializer(serializers.ModelSerializer):
    def __init__(self,*args,**kwargs):
        request = kwargs.get("context",{}).get("request") 
        str_fields = request.GET.get("Todos_history","") if request else None
        fields = str_fields.split(',') if str_fields else None
        super().__init__(*args,**kwargs)
     
        if fields != None:
            alloted = set(fields)
            all_fields = self.fields
            for not_fields in all_fields - alloted:
                self.fields.pop(not_fields)
    class meta:
        model = Todos_history
        fields = [
            
            'date',
            'time_spend'
        ]
    def validate(self, attrs):
        
        return super().validate(attrs)














































# # what can be done with the serialization for later check 

# from rest_framework.serializers import ModelSerializer, SerializerMethodField
# from .models import Book, Publisher, Author

# class PublisherModelSerializer(ModelSerializer):
#     """
#     A ModelSerializer that takes an additional `fields` argument that
#     controls which fields should be displayed.
#     """

#     def __init__(self, *args, **kwargs):
#         # Don't pass the 'fields' arg up to the superclass
#         request = kwargs.get('context', {}).get('request')
#         str_fields = request.GET.get('publisher', '') if request else None
#         fields = str_fields.split(',') if str_fields else None

#         # Instantiate the superclass normally
#         super(PublisherModelSerializer, self).__init__(*args, **kwargs)

#         if fields is not None:
#             # Drop any fields that are not specified in the `fields` argument.
#             allowed = set(fields)
#             existing = set(self.fields)
#             for field_name in existing - allowed:
#                 self.fields.pop(field_name)


#     class Meta:
#         model = Publisher
#         fields = '__all__'



# class AuthorModelSerializer(ModelSerializer):
#     """
#     A ModelSerializer that takes an additional `fields` argument that
#     controls which fields should be displayed.
#     """

#     def __init__(self, *args, **kwargs):
#         # Don't pass the 'fields' arg up to the superclass
#         request = kwargs.get('context', {}).get('request')
#         str_fields = request.GET.get('authors', '') if request else None
#         fields = str_fields.split(',') if str_fields else None

#         # Instantiate the superclass normally
#         super(AuthorModelSerializer, self).__init__(*args, **kwargs)

#         if fields is not None:
#             # Drop any fields that are not specified in the `fields` argument.
#             allowed = set(fields)
#             existing = set(self.fields)
#             for field_name in existing - allowed:
#                 self.fields.pop(field_name)


#     class Meta:
#         model = Author
#         fields = '__all__'


# class BookModelSerializer(ModelSerializer):
#     """
#     A ModelSerializer that takes an additional `fields` argument that
#     controls which fields should be displayed.
#     """
#     def __init__(self, *args, **kwargs):
#         # Don't pass the 'fields' arg up to the superclass
#         request = kwargs.get('context', {}).get('request')
#         str_fields = request.GET.get('fields', '') if request else None
#         fields = str_fields.split(',') if str_fields else None

#         # Instantiate the superclass normally
#         super(BookModelSerializer, self).__init__(*args, **kwargs)

#         if fields is not None:
#             # Drop any fields that are not specified in the `fields` argument.
#             allowed = set(fields)
#             existing = set(self.fields)
#             for field_name in existing - allowed:
#                 self.fields.pop(field_name)

#     authors = SerializerMethodField("get_author_serializer")
#     publisher = SerializerMethodField("get_publisher_serializer")

#     class Meta:
#         model = Book
#         fields = '__all__'

#     def get_author_serializer(self, obj):
#         request = self.context.get('request')
#         serializer_context = {'request': request }
#         authors = obj.authors.all()
#         serializer = AuthorModelSerializer(authors, many=True, context=serializer_context)
#         return serializer.data

#     def get_publisher_serializer(self, obj):
#         request = self.context.get('request')
#         serializer_context = {'request': request }
#         publisher = obj.publisher
#         serializer = PublisherModelSerializer(publisher, context=serializer_context)
#         return serializer.data








#   from rest_framework import serializers

# # Strict integer (reject strings)
# class StrictIntField(serializers.Field):
#     def to_internal_value(self, data):
#         if not isinstance(data, int):
#             raise serializers.ValidationError("Must be an integer, not string.")
#         return data

#     def to_representation(self, value):
#         return value

# # Company email (only @company.com)
# class CompanyEmailField(serializers.EmailField):
#     def to_internal_value(self, data):
#         email = super().to_internal_value(data)
#         if not email.endswith('@company.com'):
#             raise serializers.ValidationError("Email must be @company.com")
#         return email








# from django.db import models
# from django.core.exceptions import ValidationError

# class Employee(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     email = models.EmailField()
#     salary = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"{self.name} ({self.email})"

#     # Example of model-level validation
#     def clean(self):
#         if self.age < 18:
#             raise ValidationError("Employee must be at least 18 years old")






# from rest_framework.serializers import ModelSerializer, SerializerMethodField

# class BookModelSerializer(ModelSerializer):
#     authors = SerializerMethodField("get_author_serializer")
#     publisher = SerializerMethodField("get_publisher_serializer")

#     class Meta:
#         model = Book
#         fields = '__all__'

#     def get_author_serializer(self, obj):
#         authors = obj.authors.all()
#         serializer = AuthorModelSerializer(authors, many=True)
#         return serializer.data

#     def get_publisher_serializer(self, obj):
#         publisher = obj.publisher
#         serializer = PublisherModelSerializer(publisher)
#         return serializer.data



# class SiteSerializer(serializers.ModelSerializer):
#     class Meta:
#        model = Site
#        depth = 1
#        exclude = ('title')

#     def to_representation(self, instance):
#         rep = super(SiteSerializer, self).to_representation(instance)
#         if not rep.get('title_modified', ''):
#             rep['title_modified'] = instance.title
#         return rep


# books = Book.objects.select_related('publisher').prefetch_related('authors')
