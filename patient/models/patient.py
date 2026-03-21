from django.db import models


class Patient(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 100)
    cpf = models.CharField(max_length = 20, unique = True)
    birthday = models.DateField(null = True, blank = True)
    phone = models.CharField(max_length = 11, null = True, blank = True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
