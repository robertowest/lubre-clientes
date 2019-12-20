import django_filters

from apps.comunes.models import Diccionario
from apps.tercero.models import Comercial, Empresa


class EmpresaFilter(django_filters.FilterSet):
    comercial = django_filters.ModelChoiceFilter(
        queryset = Comercial.objects.all(),
        label = "Comercial",
    )

    class Meta:
        model = Empresa
        fields = ['comercial']