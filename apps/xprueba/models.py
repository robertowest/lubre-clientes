from django.db import models

import django_filters
from apps.comunes.models import Ciudad, Localidad

class PruebaFilter(django_filters.FilterSet):
    # ModelMultipleChoiceFilter
    ciudad = django_filters.ModelChoiceFilter(
        queryset=Ciudad.objects.all(),
        label="Localidad",
    )

    class Meta:
        model = Localidad
        fields = ['ciudad']




