from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    is_important = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['is_completed', '-is_important', 'due_date', '-created_at']

    def __str__(self):
        return self.title
