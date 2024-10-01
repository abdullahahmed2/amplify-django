from django.db import models

# Create your models here.
# tasks/models.py

class Task(models.Model):
    title = models.CharField(max_length=255)
    priority = models.IntegerField(default=1)
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
