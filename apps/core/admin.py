from django.contrib import admin
from .models import Todos , Todos_history , Dailytodos , Records

# Register your models here.

admin.site.register(Todos_history)
admin.site.register(Todos)
admin.site.register(Dailytodos)
admin.site.register(Records)
