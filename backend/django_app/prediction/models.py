from django.db import models

class TodoListItem(models.Model):
    content = models.TextField() 
    done = models.BooleanField(default=False)
    name = models.CharField(max_length=100, null=True, blank=True)