from django.urls import path
from proceeding.views import (
    ProceedingCreateView,
    ProceedingsListView,
    InquiryListView,
    ProceedingUpdateView,
    ProceedingDetailView,
    ProceedingDeleteView,
)

app_name = "proceeding"

urlpatterns = [
    # Create
    path("novo/", ProceedingCreateView.as_view(), name="create"),
    
    # Lists (ambas usam o mesmo template)
    path("procedimentos/", ProceedingsListView.as_view(), name="proceedings_list"),
    path("consultas/", InquiryListView.as_view(), name="inquiry_list"),
    
    # Detail, Update and Delete
    path("<int:pk>/", ProceedingDetailView.as_view(), name="detail"),
    path("<int:pk>/editar/", ProceedingUpdateView.as_view(), name="update"),
    path("<int:pk>/excluir/", ProceedingDeleteView.as_view(), name="delete"),
]
