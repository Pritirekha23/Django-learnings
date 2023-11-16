
from django.urls import path
from .views import home,addtask,updatetask

urlpatterns = [
     path('',home,name='home'),
     path('addtask/',addtask,name='addtask'),
     path('updatetask/',updatetask,name='updatetask'),
 
]