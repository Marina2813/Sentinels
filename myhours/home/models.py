from django.db import models

class Planner(models.Model):
    STATUS_CHOICES = [
        ('todo', 'Todo'),
        ('inprogress', 'In Progress'),
        ('complete', 'Complete'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='todo')
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
