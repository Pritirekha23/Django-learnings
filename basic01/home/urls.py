
from django.urls import path
# from . import views
from .views import index

urlpatterns = [
    #path('admin/', admin.site.urls),
    # path('home/',views.home,name='home')

    path('index/',index,name='index')
]
