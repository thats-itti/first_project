from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta , date
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import pre_delete , pre_save , post_delete , post_save
from django.contrib.auth.models import  AbstractUser

# Create your models here.

class customuser(AbstractUser):
    username = None
    email = models.EmailField(verbose_name="email address",unique=True)
    USERNAME_FIELD = "email"
    


   

class Todos(models.Model):
    task = models.CharField(verbose_name="title", null = False , blank = False , max_length= 70)
    start_working_at = models.DateTimeField(verbose_name ="start_time", blank= True , null= True )

    issued_date = models.DateTimeField(verbose_name="issued_date" ,auto_now_add= True)
    task_date = models.DateTimeField(verbose_name= " ..complete  time when suppose to finish", blank = False , null= False )
    description = models.TextField(verbose_name= "description ", blank = True , null= True )

    time_based = models.BooleanField(verbose_name="time based" ,null = False , blank = False)

    
    working = models.BooleanField(verbose_name="working", default= False , null= False , blank= False)

    completed = models.BooleanField(verbose_name= "completed or not task")

    daily_based = models.BooleanField(verbose_name="daily_based", null = False , blank = False)

    total_time = models.DurationField(verbose_name=" total time invested for task ", null= True , blank = True , default= timedelta())
    total_daily_completed = models.IntegerField(verbose_name="dialy_completed" , null= True , blank = True)

    completed_time = models.DurationField(verbose_name="completed duration",null= True , blank = True , default= timedelta())

    daily_time = models.DurationField(
        verbose_name="time daily to set ", null = True , blank = True , default= timedelta()
    )
     
    user = models.ForeignKey(User , on_delete= models.CASCADE , null=  False , blank = False , related_name= "all_times_activity")
    

    @property
    def remaining_time(self):
        if self.total_time is not None:
            return self.total_time - self.completed_time
        return None

class Todos_history(models.Model):
    
    user = models.ForeignKey(User , on_delete = models.CASCADE , null = False , blank = False , related_name = "history")
    
    todo = models.ForeignKey(Todos , on_delete = models.CASCADE , null = False , blank = False , related_name = "its_history")
    date = models.DateField(verbose_name= "date")
    time_spend = models.DurationField(verbose_name="time-spend ", default= timedelta())


class Dailytodos(models.Model): 

    
    working = models.BooleanField(verbose_name="working", default= False , null= False , blank= False)
    start_working_at = models.DateTimeField(verbose_name ="start_time", blank= True , null= True )
    history = models.ForeignKey(Todos_history , related_name="daily_todo", on_delete=models.CASCADE)
    task = models.CharField(verbose_name="title", null = False , blank = False, max_length= 70)
    description = models.TextField(verbose_name= "description ", blank = True , null= True )
    time_based = models.BooleanField(verbose_name="time based", null = False , blank = False)
    completed = models.BooleanField(verbose_name= "completed or not ")
    completed_time = models.DurationField(verbose_name="completed duration",null= True , blank = True , default= timedelta())
    daily_time = models.DurationField(verbose_name="time invested for task ", null= True , blank = True , default= timedelta())
    link = models.ForeignKey(Todos, on_delete= models.CASCADE , null= True , blank= True , related_name="individual_daily_total_investment")
    user = models.ForeignKey(User , on_delete= models.CASCADE , null=  False , blank = False , related_name= "all_daily_activity")
 
class Records(models.Model):
    issued_date = models.DateField(verbose_name="date issued" , blank = False , null = False , auto_now_add= True )  
    # here i need to add so that the default could be the date the acivity was listed
    task_date = models.DateField(verbose_name= "the task date" , blank = False , null = False)
    task = models.CharField(verbose_name="title", null = False , blank = False , max_length= 70)
    description = models.TextField(verbose_name = "verbose", blank= True , null= True)
    user = models.ForeignKey(User , on_delete= models.CASCADE , null=  False , blank = False , related_name= "records")






































































# inside of a models with manytomany relation 
# class Meta:
#         constraints = [
#             models.UniqueConstraint(
#                 fields=['person', 'group'],
#                 name='unique_person_group'
#             )
#         ]