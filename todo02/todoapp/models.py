from django.db import models

class TodoItem(models.Model):
    title = models.CharField(max_length=10)
   # completed = models.BooleanField(default=False)
    description=models.CharField(max_length=200)

    def __str__(self):
        return self.title
