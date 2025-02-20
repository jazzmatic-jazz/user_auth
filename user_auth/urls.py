from django.contrib.auth import views as auth
from django.urls import path
from .views import index, register, login_user, logout_view, doctor_dashboard, patient_dashboard


urlpatterns = [
    path("", index, name="index"),
    path("register", register, name="register"),
    path("login", login_user, name="login"),
    path("logout", logout_view, name="logout"),
    path("patient", patient_dashboard, name="patient"),
    path("doctor", doctor_dashboard, name="doctor"),
]
