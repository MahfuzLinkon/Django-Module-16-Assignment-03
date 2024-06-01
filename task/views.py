from django.shortcuts import render,redirect
from .forms import TaskForm
from .models import Task

# Create your views here.
def add_task(request):
    if request.method == "POST":
        taskForm = TaskForm(request.POST)
        if taskForm.is_valid():
            taskForm.save()
            return redirect('add_task')
    else:
        taskForm = TaskForm()
    return render(request, 'task_form.html', {'taskForm': taskForm})

def edit_task(request, id):
    task = Task.objects.get(pk= id)
    taskForm = TaskForm(instance=task)
    if request.method == "POST":
        taskForm = TaskForm(request.POST, instance=task)
        if taskForm.is_valid():
            taskForm.save()
            return redirect('home')
    return render(request, 'task_form.html', {'taskForm': taskForm})

def delete_task(request, id):
    task = Task.objects.get(pk= id)
    task.delete()
    return redirect('home')