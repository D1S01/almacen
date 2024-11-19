from django.urls import path
from .views import RegistrarseView, PerfilView

urlpatterns = [
    path('registrarse/', RegistrarseView.as_view(), name = 'signup'),
    path('perfil/', PerfilView.as_view(), name = 'profile')
]