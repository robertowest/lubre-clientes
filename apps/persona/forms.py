from django import forms
from material import Layout, Row

from .models import Persona

class PersonaForm(forms.ModelForm):
    layout = Layout(
        Row('nombre', 'apellido'),
        Row('documento'),
        Row('active'),
    )

    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'documento', 'active']