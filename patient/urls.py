from django.urls import path
from .views import PatientListView, PatientCreateView

app_name = "patients"

urlpatterns = [
    path("", PatientListView.as_view(), name = "list"),
    path("create/", PatientCreateView.as_view(), name = "create")
]
