from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from proceeding.models import Proceeding


class ProceedingCreateView(LoginRequiredMixin, CreateView):
    model = Proceeding
    template_name = "proceeding/create.html"

    fields = [
        "id_doctor",
        "id_patient",
        "tuss_code",
        "proceeding_type",
        "description"
    ]

    def get_success_url(self):
        return reverse_lazy("proceeding:detail", kwargs={'pk': self.object.pk})

    

    def form_valid(self, form):
        form.instance.created_by = self.request.user

        proceeding_type = form.cleaned_data.get("proceeding_type")
        
        if proceeding_type == "Inquiry":
            message = "Consulta criada com sucesso!"
        else:
            message = "Procedimento registrado com sucesso"

        messages.success(self.request, f"{message}")
        return super().form_valid(form)


# Registros = Proceedings de todos os tipos (Inquiry + Proceeding)
class BaseRecordsListView(LoginRequiredMixin, ListView):
    model = Proceeding
    template_name = "proceeding/list.html"
    context_object_name = "records"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["proceeding_type"] = self.proceeding_type
        context["title"] = self.title
        return context


# Lista apenas procedimentos
class ProceedingsListView(BaseRecordsListView):
    proceeding_type = "Proceeding"
    title = "Procedimentos realizados"

    def get_queryset(self):
        return Proceeding.objects.filter(proceeding_type=self.proceeding_type)


# Lista apenas consultas
class InquiryListView(BaseRecordsListView):
    proceeding_type = "Inquiry"
    title = "Consultas realizadas"

    def get_queryset(self):
        return Proceeding.objects.filter(proceeding_type=self.proceeding_type)


class ProceedingUpdateView(LoginRequiredMixin, UpdateView):
    model = Proceeding
    template_name = "proceeding/update_and_detail.html"

    fields = [
        "id_doctor",
        "id_patient",
        "tuss_code",
        "proceeding_type",
        "description"
    ]

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mode"] = "update"
        return context


class ProceedingDetailView(LoginRequiredMixin, DetailView):
    model = Proceeding

    template_name = "proceeding/update_and_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mode"] = "read"
        return context


class ProceedingDeleteView(LoginRequiredMixin, DeleteView):
    model = Proceeding

    def get_success_url(self):
        obj = self.get_object()

        if obj.proceeding_type == "Inquiry":
            return reverse_lazy("proceeding:inquiry_list")  # Adicione o namespace
        else:
            return reverse_lazy("proceeding:proceedings_list")  # Adicione o namespace
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        # Mensagem personalizada baseada no tipo
        if self.object.proceeding_type == 'Proceeding':
            messages.success(request, f'Procedimento "{self.object}" removido com sucesso!')
        else:
            messages.success(request, f'Consulta "{self.object}" removida com sucesso!')
        
        return super().delete(request, *args, **kwargs)
