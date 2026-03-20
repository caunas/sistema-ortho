from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from patient.models import Patient


class PatientListView(LoginRequiredMixin, ListView):
    model = Patient
    template_name = "patient/list.html"
    