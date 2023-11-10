
from django.urls import path
from .views import home

urlpatterns = [
     path('home/',home,name='home'),
     # path('index/',index,name='index'),
     # path('add_todo/',add_todo,name='add_todo')
 
]