from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import FondeoCajaChica, GastoCajaChica, ValeCaja
from .forms import FondeoCajaChicaForm, GastoCajaChicaForm, ValeCajaForm


def fondeo_caja_chica(request):
    if request.method == "POST":
        form = FondeoCajaChicaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Fondeo registrado exitosamente.")
    else:
        form = FondeoCajaChicaForm()
    return render(request, "caja_chica/fondeo_caja_chica.html", {"form": form})


def registrar_gasto_caja_chica(request):
    if request.method == "POST":
        form = GastoCajaChicaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Gasto registrado exitosamente.")
    else:
        form = GastoCajaChicaForm()
    return render(request, "caja_chica/registrar_gasto_caja_chica.html", {"form": form})


def generar_vale_caja(request):
    if request.method == "POST":
        form = ValeCajaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Vale generado exitosamente.")
    else:
        form = ValeCajaForm()
    return render(request, "caja_chica/generar_vale_caja.html", {"form": form})
