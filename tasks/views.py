from django.shortcuts import render

from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    stats = {
        'total': tasks.count(),
        'pending': tasks.filter(is_completed=False).count(),
        'completed': tasks.filter(is_completed=True).count(),
        'important': tasks.filter(is_important=True).count(),
    }
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'stats': stats})
