from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from patient.models import Patient


class PatientListView(LoginRequiredMixin, ListView):
    model = Patient
    template_name = "patient/list.html"
 

class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient
    template_name = "patient/create.html"

    fields = [
            "first_name",
            "last_name",
            "cpf",
            "birthday",
            "phone"
            ]

    success_url = reverse_lazy("patients:list")


    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, "Paciente Cadastrado com sucesso!")
        return super().form_valid(form)

