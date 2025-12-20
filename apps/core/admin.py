from django.contrib import admin
from .models import Todos , Todos_history , Dailytodos , Records ,User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(Todos_history)
admin.site.register(Todos)
admin.site.register(Dailytodos)
admin.site.register(Records)


@admin.register(User)
class customuser(UserAdmin):
    model = User
    # this list_display is for what should be display in like usermodel as a single instance outside what you wish to be shown to represent 
    list_display = ("email","is_staff","is_superuser","is_active",)
    # through the means of this terms you could filter out the users in the user models
    list_filter = ("is_staff","is_superuser","is_active")
    # ordering suppose to be the one which is used to order the models data by
    ordering = ("email",)
    search_fields = ('email',)
    fieldsets = (
        (None,{'fields':('email','password',)
               }),
        ('permission',{
            'fields':('is_staff','is_superuser',
                      'groups',
                    #   'user_permission'
                      )
        }),
        ('status',{'fields':
                   ('is_active',)}),
    )
    add_fieldsets = (
        (None,{
            'classes':("wide",),
            'fields':('email','passwoed1','password2','is_staff','is_superuser','is_staff','is_superuser'),
        }),
        
    )
    filter_horizontal = ('groups','user_permissions')

