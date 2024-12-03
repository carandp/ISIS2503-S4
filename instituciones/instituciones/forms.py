from django import forms
from .models import Factura

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields =  ['institucion', 'direccion', 'nombre', 'telefono', 'correo']
        labels = {
            'institucion': 'Institucion',
            'direccion': 'Direccion',
            'nombre': 'Nombre',
            'telefono': 'Telefono',
            'correo': 'Correo',
        }