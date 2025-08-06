from django import forms
from .models import FondeoCajaChica, GastoCajaChica, ValeCaja


class FondeoCajaChicaForm(forms.ModelForm):
    class Meta:
        model = FondeoCajaChica
        fields = [
            "numero_cheque",
            "importe_cheque",
            "empleado_asignado",
            "fecha",
            "saldo",
        ]


class GastoCajaChicaForm(forms.ModelForm):
    class Meta:
        model = GastoCajaChica
        fields = ["fondeo", "descripcion", "importe", "fecha"]


class ValeCajaForm(forms.ModelForm):
    class Meta:
        model = ValeCaja
        fields = ["fondeo", "descripcion", "importe", "fecha"]
