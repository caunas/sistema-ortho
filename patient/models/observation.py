from django.db import models

from patient.models import patient
from doctor.models import doctor


class Observation(models.Model):
    id_patient = models.ForeignKey(patient.Patient, on_delete=models.CASCADE)
    id_author = models.ForeignKey(doctor.Doctor, on_delete = models.CASCADE)
    
    #is_private = models.BooleanField()
    
    title = models.CharField(max_length=30, null = False, blank = False)
    content = models.CharField(max_length=280)
    
    def __str__(self):
        return f"{self.title}"
