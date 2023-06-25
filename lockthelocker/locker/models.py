from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Locker(models.Model):
    locker_id = models.IntegerField(primary_key=True)
    occupied = models.BooleanField(default=False)
    broken = models.BooleanField(default=False)

class Appointment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    locker = models.ForeignKey(Locker, on_delete=models.CASCADE, null=True)