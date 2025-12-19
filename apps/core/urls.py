from django.urls import path , include
from . import views
urlpatterns = [
    
    path("todo_listview/",views.Todos_listview.as_view()),
    path("todo_listview/<int:pk>/",views.Todos_listview.as_view()),

    path("todo_createapiview",views.Todos_createapiview.as_view()),
    # path("todo_destroyview/<int:pk>/",views.Todos_destroyapiview.as_view()),
]