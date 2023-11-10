from django.contrib import admin
from django.urls import path,include
# from .views import index,add_todo

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',index,name='index'),
    # path('',add_todo,name='add_todo')
    path('',include('todoapp.urls')),
]