from django.urls import path
from .views import PatientListView

app_name = "patients"

urlpatterns = [
    path("", PatientListView.as_view(), name = "list")
]
