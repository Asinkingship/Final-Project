from django.db import models
from groups.models import Group


class Event(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='events', default=1)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=200)
    price = models.CharField(max_length=200)

    def __str__(self):
        return self.title

# Create your models here.
