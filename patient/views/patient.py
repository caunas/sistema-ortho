from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from patient.models import Patient


class PatientListView(LoginRequiredMixin, ListView):
    model = Patient
    template_name = "patient/list.html"
    context_object_name = "patients"


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


class PatientUpdateView(LoginRequiredMixin, UpdateView):
    model = Patient
    template_name = "patient/update_and_detail.html"

    fields = [
            "first_name",
            "last_name",
            "cpf",
            "birthday",
            "phone"
            ]

    ## slug virtual para usar cpf ao invés de chave primaria
    slug_field = "cpf"
    slug_url_kwarg = "cpf"

    success_url = reverse_lazy("patients:list")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = True
        context['title'] = 'Editar prontuário'
        context['bnt_action'] = "Salvar Alterações"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Prontuário editado com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrija os erros abaixo.")
        return super().form_invalid(form)


class PatientDetailView(LoginRequiredMixin, DetailView):
    model = Patient
    template_name = "patient/update_and_detail.html"

    #slug virtual
    slug_field = "cpf"
    slug_url_kwarg = "cpf"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = False
        context['title'] = 'Detalhes do paciente'
        context['bnt_action'] = "Editar prontuário"
        return context


class PatientDeleteView(LoginRequiredMixin, DeleteView):
    model = Patient
    success_url = reverse_lazy("patients:list")


    #slug virtual
    slug_field = "cpf"
    slug_url_kwarg = "cpf"


