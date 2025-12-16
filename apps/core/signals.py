
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Todos , Todos_history , Dailytodos







@receiver(post_save,sender= Todos)
def auto_add(sender,instance,created,**kwargs):
    if created:
        history = Todos_history.objects.create(
            user = instance.user,
            todo = instance ,
            date = instance.task_date

        
        )

        if instance.daily_based:
            if instance.time_based:
                Dailytodos.objects.create(
                    user = instance.user ,
                    
                    task = instance.task,
                    link = instance,
                    completed = False,
                    daily_time = instance.daily_time ,
                    time_based = instance.time_based,
                    history = history

                )