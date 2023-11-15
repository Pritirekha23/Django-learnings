
from django.urls import path
from .views import home,addtask

urlpatterns = [
   path('',home,name='home'),
   path('addtask/',addtask,name="addtask")
]