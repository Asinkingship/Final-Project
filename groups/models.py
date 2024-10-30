from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    name = models.CharField(max_length=255)

class Invitation(models.Model):
    email = models.EmailField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    invited_by = models.ForeignKey(User, related_name='invitations_sent', on_delete=models.CASCADE)
    invited_user = models.ForeignKey(User, related_name='invitations_received', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.email} invited to {self.group.name}"


# Create your models here.
