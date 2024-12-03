from django import forms
from .models import Factura

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields =  ['id', 'cedula', 'descripcion', 'total']
        labels = {
            'id': 'Id',
            'cedula': 'Cedula',
            'descripcion': 'Descripcion',
            'total': 'Total',
        }