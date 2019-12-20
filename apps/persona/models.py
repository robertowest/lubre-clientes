import datetime
import django_filters

from django.urls import reverse
from django.db import models

from apps.comunes.models import AudtoriaMixin

# Create your models here.
class Persona(AudtoriaMixin):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    documento = models.CharField("D.N.I.", max_length=12, null=True, blank=True)

    def __str__(self):
        return "%s, %s" % (self.apellido, self.nombre)

    def get_absolute_url(self):
        # reverse('persona:info', kwargs={'pk': self.pk})
        return reverse('persona:info', args=(self.pk,))

    def get_update_url(self):
        return reverse('persona:modif', args=(self.pk,))

    def get_delete_url(self):
        return reverse('persona:borrar', args=(self.pk,))

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['apellido', 'nombre']


class PersonaFilter(django_filters.FilterSet):
    texto = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Persona
        fields = ['apellido', 'nombre']


