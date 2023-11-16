from django.shortcuts import render, redirect
from .models import TodoItem

# from .forms import TodoItemForm

def home(request):
    list_of_todo=TodoItem.objects.all().values
    return render(request,'home.html',{'todo_list':list_of_todo})
    

def entry(request):
    
    return render(request,'entry.html')

