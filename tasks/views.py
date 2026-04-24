from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import TaskForm
from .models import Task


@login_required
def task_list(request):
    tasks = Task.objects.filter(owner=request.user)
    stats = {
        'total': tasks.count(),
        'pending': tasks.filter(is_completed=False).count(),
        'completed': tasks.filter(is_completed=True).count(),
        'important': tasks.filter(is_important=True).count(),
    }
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'stats': stats})


@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            return redirect('tasks:task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form, 'mode': 'create'})


@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form, 'mode': 'update', 'task': task})


@login_required
@require_POST
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    task.delete()
    return redirect('tasks:task_list')


@login_required
@require_POST
def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('tasks:task_list')
