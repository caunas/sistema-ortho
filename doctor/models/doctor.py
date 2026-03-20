from django.db import models
from django.contrib.auth.models import User

from doctor.models import specialization


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True, blank = True)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    CRO = models.CharField(max_length = 35)
    specialization = models.ForeignKey(specialization.Specialization, on_delete = models.CASCADE)
    
    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"
    