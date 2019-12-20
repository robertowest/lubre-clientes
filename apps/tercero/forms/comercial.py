from django import forms
from material import Layout, Row

from apps.tercero.models import Comercial


class ComercialForm(forms.ModelForm):
    layout = Layout(
        'persona',
        'domicilios',
        'comunicaciones',
        'active',
    )

    class Meta:
        model = Comercial
        fields = ['persona', 'domicilios', 'comunicaciones', 'active']
