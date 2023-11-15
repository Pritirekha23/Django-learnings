from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task

def home(request):
   list_of_todo=Task.objects.all()
   return render(request,'home.html',{'todo_list':list_of_todo})
   
def addtask(request):
   if request.method=="POST":
      tasktitle=request.POST['TaskTitle']
      taskdescription = request.POST.get('userText', '')
      print(tasktitle,taskdescription)
      x=Task.objects.create(title=tasktitle,description=taskdescription)
      x.save()
      return redirect('home')
   return render(request,'addtask.html')