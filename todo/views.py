from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TodoForm, UpdateTodoForm
from .models import Todo

def index(request):
    # get all tasks from the database; get form
    todos = Todo.objects.all()
    form = TodoForm()

    context = {
        'form': form,
        'todos': todos,
    }
    return render(request, 'todo/index.html', context)

def add(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('/')

def delete(request, task_id):
    todo = Todo.objects.get(id=task_id)
    if request.method == 'POST':
        messages.success(request, todo.task_name + " has been removed.")
        todo.delete()
        return redirect('/')

    context = {
        'todo': todo,
    }
    return render(request, 'todo/delete.html', context)

def update(request, task_id):
    # get the task of selected from the database; get form
    todo = Todo.objects.get(id=task_id)
    if request.method == 'POST':
        form = UpdateTodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UpdateTodoForm(instance=todo)
        
    context = {
        'form': form,
        'id': task_id,
    }      
    return render(request, 'todo/update.html', context)

def complete_task(request, task_id):
    todo = Todo.objects.get(id=task_id)
    todo.completed = True
    todo.save()
    messages.success(request, todo.task_name + " has been completed.")
    return redirect('/')

