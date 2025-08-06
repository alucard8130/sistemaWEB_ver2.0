from django.urls import path
from . import views

urlpatterns = [
    path("fondeo/", views.fondeo_caja_chica, name="fondeo_caja_chica"),
    path("registrar_gasto/", views.registrar_gasto_caja_chica, name="registrar_gasto_caja_chica"),
    path("generar_vale/", views.generar_vale_caja, name="generar_vale_caja"),
]
