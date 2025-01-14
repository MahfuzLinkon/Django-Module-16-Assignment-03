from django.db import models
from category.models import Category

# Create your models here.
class Task(models.Model):
    task_title = models.CharField(max_length=100)
    task_description = models.TextField()
    categories = models.ManyToManyField(Category)
    task_assign_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.task_title