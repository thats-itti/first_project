from django.db import models

# Create your models here.

class Todos(models.Model):
    issued_date = models.DateField(verbose_name="issued_date" ,auto_now_add= True)
    description = models.TextField(verbose_name= "description ", blank = True , null= True )
    task_time = models.DateField(verbose_name="set_time", blank= True, null=True)
    completed = models.BooleanField(verbose_name= "completed or not ")
    total_time = models.DurationField(verbose_name="time invested for task ", null= True , blank = True , default= 0.00)
    completed_time = models.DurationField(verbose_name="completed duration",null= True , blank = True , default= 0.00)
     
    

class dailytodos(models.Model): 
    issued_date = models.DateField(verbose_name="issued_date" ,auto_now_add= True)
    description = models.TextField(verbose_name= "description ", blank = True , null= True )
    task_time = models.DateField(verbose_name="set_time", blank= True, null=True)
    completed = models.BooleanField(verbose_name= "completed or not ")
    completed_time = models.DurationField(verbose_name="completed duration",null= True , blank = True , default= 0.00)
    daily_time = models.DurationField(verbose_name="time invested for task ", null= True , blank = True , default= 0.00)
    link = models.ForeignKey(Todos, on_delete= models.CASCADE , null= True , blank= True , related_name="individual_daily_total_investment")






class user(models.Model):
    username = models.TextField(verbose_name="name",max_length= 40 , blank = False , unique = True )




class Login(models.Model):
    username = models.EmailField(verbose_name= "email", blank = False , null=False , unique = True  ,max_length= 254)
    password = models.CharField(verbose_name = "password ",blank = False , null = False , max_length= 128 )

    def __str__(self):
        return self.usrname