
from django.urls import path,include
from .views import index,add_todo

urlpatterns = [
     path('index/',index,name='index'),
     path('add_todo/',add_todo,name='add_todo')
   # path('',include('todoapp.urls')),
]