from django.urls import path
from .views import PatientListView, PatientCreateView, PatientDetailView, PatientUpdateView, PatientDeleteView

app_name = "patients"

urlpatterns = [
    path("", PatientListView.as_view(), name = "list"),
    path("novo/", PatientCreateView.as_view(), name = "create"),
    path("<str:cpf>/", PatientDetailView.as_view(), name = "detail"),
    path("<str:cpf>/editar", PatientUpdateView.as_view(), name = "update"),
    path("<str:cpf>/excluir", PatientDeleteView.as_view(), name = "delete")
]
