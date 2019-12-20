from django import forms
from material import Layout, Row

from apps.tercero.models import Empresa


class EmpresaForm(forms.ModelForm):
    layout = Layout(
        Row('cuit', 'nombre'),
        'razon_social',
        Row('domicilios', 'comunicaciones'),
        Row('comercial', 'actividad', 'referencia_id'),
        'active',
    )


    class Meta:
        model = Empresa
        fields = ['cuit', 'nombre', 'razon_social',
                  'domicilios', 'comunicaciones', 'comercial', 'actividad',
                  'referencia_id', 'active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['actividad'].queryset = self.fields['actividad'].queryset.filter(tabla='actividad')


class EmpresaFilter(forms.ModelForm):
    layout = Layout(
        'comercial',
        'actividad',
    )

    class Meta:
        model = Empresa
        fields = ['comercial', 'actividad']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comercial'].queryset = self.fields['comercial'].queryset.filter(active=True)
        self.fields['actividad'].queryset = self.fields['actividad'].queryset.filter(tabla='actividad')
