from django import forms
from .models import AreaComun
from clientes.models import Cliente
from empresas.models import Empresa


class AreaComunForm(forms.ModelForm):
    class Meta:
        model = AreaComun
        fields = ['numero','cliente','empresa' , 'superficie_m2','tipo_area','cantidad_areas', 'cuota','deposito','giro','ubicacion','fecha_inicial', 'fecha_fin', 'status',  'observaciones']
        widgets = {
            'numero': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número'
            }),
            'cliente': forms.Select(attrs={
                'class': 'form-control'
            }),
            'empresa': forms.Select(attrs={
                'class': 'form-control'
            }),
            'superficie_m2': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Superficie_m2'
            }),
            'tipo_area': forms.Select(attrs={
                'class': 'form-control'       
            }),
            'cantidad_areas': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'cuota': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cuota'
            }),
            'deposito': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Depósito'
            }),
            'giro': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Giro'
            }),
            'ubicacion': forms.Textarea(attrs={
                'rows': 2,
                'class': 'form-control',
                'placeholder': 'Ubicación'        
            }),
            'fecha_inicial': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'fecha_fin': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
            'observaciones': forms.Textarea(attrs={
                'rows': 2,
                'class': 'form-control',
                'placeholder': 'Observaciones'        
            }),
        }
        labels = {
            'numero': 'Número',
            'tipo_area': 'Tipo de área',
            'cantidad_areas': 'Cantidad de áreas',
            'deposito': 'Depósito',
            'ubicacion': 'Ubicación',
            'status': 'Estatus',
        }
    def __init__(self, *args, **kwargs):
        #self.user = kwargs.pop('user', None)
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
   
        if user and not user.is_superuser:
            self.fields['empresa'].widget = forms.HiddenInput()
            empresa = user.perfilusuario.empresa
            self.fields['empresa'].initial = empresa  # <-- Asigna el valor aquí
            self.fields['cliente'].queryset = Cliente.objects.filter(empresa=empresa)
        else:
            self.fields['cliente'].queryset = Cliente.objects.all()
         
        # Deshabilita el campo cliente si se está editando un local existente
        if self.instance and self.instance.pk:
            self.fields['cliente'].disabled = True
            self.fields['numero'].disabled = True
            self.fields['status'].disabled = True    

    def clean(self):
        cleaned_data = super().clean()
        numero = cleaned_data.get('numero')  # Cambiado de 'nombre' a 'numero'
        empresa = cleaned_data.get('empresa')
        fecha_inicial = cleaned_data.get('fecha_inicial')
        fecha_fin = cleaned_data.get('fecha_fin')

        if numero and empresa:
            qs = AreaComun.objects.filter(numero__iexact=numero, empresa=empresa, activo=True)
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise forms.ValidationError("Ya existe un área común con ese número en esta empresa.")

        if not fecha_inicial:
            raise forms.ValidationError("Debe ingresar la fecha inicial.")        
        if not fecha_fin:
            raise forms.ValidationError("Debe ingresar la fecha fin.")

        if fecha_inicial and fecha_fin and fecha_inicial > fecha_fin:
            raise forms.ValidationError("La fecha inicial no puede ser posterior a la fecha fin.")

        return cleaned_data
          

class AsignarClienteForm(forms.ModelForm):
    class Meta:
        model = AreaComun
        fields = ['cliente','fecha_inicial', 'fecha_fin']
        widgets = {
            'fecha_inicial': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'].queryset = Cliente.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        cliente = cleaned_data.get('cliente')
        fecha_inicial = cleaned_data.get('fecha_inicial')
        fecha_fin = cleaned_data.get('fecha_fin')

        if not cliente:
            self.add_error('cliente', 'Debe seleccionar un cliente.')
        if not fecha_inicial:
            self.add_error('fecha_inicial', 'Debe ingresar la fecha inicial.')
        if not fecha_fin:
            self.add_error('fecha_fin', 'Debe ingresar la fecha fin.')

        return cleaned_data    

class AreaComunCargaMasivaForm(forms.Form):
    archivo = forms.FileField(label='Archivo Excel (.xlsx)')
