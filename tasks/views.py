from django.contrib.auth.decorators import login_required
from django.shortcuts import render

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
