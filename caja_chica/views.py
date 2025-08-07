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


def lista_fondeos(request):
    fondeos = FondeoCajaChica.objects.all()
    return render(request, "caja_chica/lista_fondeos.html", {"fondeos": fondeos})


def lista_gastos_caja_chica(request):
    gastos = GastoCajaChica.objects.select_related("fondeo").all()
    return render(
        request, "caja_chica/lista_gastos_caja_chica.html", {"gastos": gastos}
    )


def lista_vales_caja_chica(request):
    vales = ValeCaja.objects.select_related("fondeo").all()
    return render(request, "caja_chica/lista_vales_caja_chica.html", {"vales": vales})
