from django.urls import path, include
from django.contrib.auth import views as auth_views

from core.views import dashboard


urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name = "core/login.html"), name = "login"),
    path("dashboard/", dashboard, name="dashboard"),
    path("pacientes/", include("patient.urls"))
]