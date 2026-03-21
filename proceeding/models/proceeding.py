from django.db import models

from doctor.models import doctor
from patient.models import patient

class Proceeding(models.Model):
    id_doctor = models.ForeignKey(doctor.Doctor, on_delete = models.CASCADE)
    id_patient = models.ForeignKey(patient.Patient, on_delete = models.CASCADE)

    tuss_code = models.IntegerField(blank = False)
    date = models.DateTimeField(auto_now_add = True)
    
    class ProceedingType(models.TextChoices):
        INQUIRY = 'Inquiry', 'Consulta'
        PROCEEDING = 'Proceeding', 'Procedimento'
    
    description = models.TextField(max_length=250)

    proceeding_type = models.CharField(
        max_length=20,
        choices=ProceedingType.choices,
        default=ProceedingType.PROCEEDING
    )


    def __str__(self):
        return f"{self.date}: {self.id_patient}"

