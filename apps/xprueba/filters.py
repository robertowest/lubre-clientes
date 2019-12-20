import django_filters

from apps.comunes.models import Ciudad, Localidad

class MyFilter(django_filters.FilterSet):
    ciudad = django_filters.ModelChoiceFilter(
        queryset=Ciudad.objects.all(),
        label="Localidad",
    )

    class Meta:
        model = Localidad
        fields = ['ciudad']