from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoItemForm

def index(request):
    todos = TodoItem.objects.all()
    return render(request, 'todoapp/index.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoItemForm()
    return render(request, 'todoapp/add_todo.html', {'form': form})
