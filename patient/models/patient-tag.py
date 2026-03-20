from django.db import models

from patient.models import patient, tag


class PatientTag(models.Model):
    id_patient = models.ForeignKey(patient.Patient, on_delete=models.CASCADE)
    id_tag = models.ForeignKey(tag.Tag, on_delete = models.CASCADE)