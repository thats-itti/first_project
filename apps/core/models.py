from django.db import models
from django.contrib.auth.models import User
from django import timedelta , date


# Create your models here.



class Todos(models.Model):
    task = models.CharField(verbose_name="title", null = False , blank = False , max_length= 70)

    issued_date = models.DateField(verbose_name="issued_date" ,auto_now_add= True)

    description = models.TextField(verbose_name= "description ", blank = True , null= True )

    time_based = models.BooleanField(verbose_name="time based" ,null = False , blank = False)

    task_time = models.DateTimeField(verbose_name="set_time", blank= True, null=True)


    completed = models.BooleanField(verbose_name= "completed or not ")

    daily_based = models.BooleanField(verbose_name="daily_based", null = False , blank = False)

    total_time = models.DurationField(verbose_name="time invested for task ", null= True , blank = True , default= timedelta())


    completed_time = models.DurationField(verbose_name="completed duration",null= True , blank = True , default= timedelta())

    daily_time = models.DurationField(
        verbose_name="time daily base ", null = True , blank = True , default= timedelta()
    )
     
    user = models.ForeignKey(User , on_delete= models.CASCADE , null=  False , blank = False , related_name= "all_times_activity")

class dailytodos(models.Model): 

     
    task = models.CharField(verbose_name="title", null = False , blank = False, max_length= 70)
    description = models.TextField(verbose_name= "description ", blank = True , null= True )
    time_based = models.BooleanField(verbose_name="time based", null = False , blank = False)
    task_time = models.DateTimeField(verbose_name="set_time", blank= True, null=True)
    completed = models.BooleanField(verbose_name= "completed or not ")
    completed_time = models.DurationField(verbose_name="completed duration",null= True , blank = True , default= timedelta())
    daily_time = models.DurationField(verbose_name="time invested for task ", null= True , blank = True , default= timedelta())
    link = models.ForeignKey(Todos, on_delete= models.CASCADE , null= True , blank= True , related_name="individual_daily_total_investment")
    user = models.ForeignKey(User , on_delete= models.CASCADE , null=  False , blank = False , related_name= "all_daily_activity")
 
class records(models.Model):
    issued_date = models.DateField(verbose_name="date activity" , blank = False , null = False )  
    # here i need to add so that the default could be the date the acivity was listed
     
    task = models.CharField(verbose_name="title", null = False , blank = False , max_length= 70)
    description = models.TextField(verbose_name = "verbose", blank= True , null= True)
    user = models.ForeignKey(User , on_delete= models.CASCADE , null=  False , blank = False , related_name= "records")





