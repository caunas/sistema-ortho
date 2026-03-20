from django.contrib import admin

# Register your models here.
from .models import Doctor, Specialization

admin.site.register(Doctor)
admin.site.register(Specialization)
