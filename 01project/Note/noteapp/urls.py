
from django.urls import path
from .views import home,addtask,delete,update

urlpatterns = [
   path('', home, name='home'),
   path('addtask/',addtask,name="addtask"),
   path('delete/<int:id>',delete, name="delete"),
   path('update/<int:id>',update, name="update")
]