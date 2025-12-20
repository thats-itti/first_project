from django.urls import path , include
from . import views
urlpatterns = [
    
    path("todo_listview/",views.Todo_listview.as_view()),
    path("todo_listview/<int:pk>/",views.Todos_otherview.as_view()),

    
    path("dailytodo_listview/",views.DailyTodo_view1.as_view()),
    path("dailytodo_listview/<int:pk>/",views.DailyTodo_view.as_view()),

    
    path("historytodo_listview/",views.TodoHistory_view1.as_view()),
    path("historytodo_listview/<int:pk>/",views.TodoHistory_view.as_view()),

    
    path("record_listview/",views.RecordTodo_view1.as_view()),
    path("record_listview/<int:pk>/",views.RecordTodo_view.as_view()),

    # path("todo_createapiview",views.Todos_createapiview.as_view()),
    # path("todo_destroyview/<int:pk>/",views.Todos_destroyapiview.as_view()),
]