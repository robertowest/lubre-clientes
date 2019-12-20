from django.urls import reverse
from django.db import models

from apps.comunes.models import AudtoriaMixin, Domicilio, Comunicacion, Diccionario
from apps.tercero.models import Comercial


class Empresa(AudtoriaMixin):
    cuit = models.CharField(max_length=13, unique=True)
    nombre = models.CharField(max_length=60)
    razon_social = models.CharField("Razón Social", max_length=60, null=True, blank=True)
    domicilios = models.ManyToManyField(Domicilio, related_name='empresa_domicilios', blank=True)
    comunicaciones = models.ManyToManyField(Comunicacion, related_name='empresa_comunicaciones', blank=True)
    comercial = models.ForeignKey(Comercial, on_delete=models.CASCADE, null=True, blank=True)
    actividad = models.ForeignKey(Diccionario, on_delete=models.CASCADE, null=True, blank=True)
    referencia_id = models.IntegerField('Referencia Externa', null=True, unique=True)

    def __str__(self):
        return self.razon_social

    def get_absolute_url(self):
        # reverse('persona:info', kwargs={'pk': self.pk})
        return reverse('tercero:empr_info', args=(self.pk,))

    def get_update_url(self):
        return reverse('tercero:empr_modif', args=(self.pk,))

    def get_delete_url(self):
        return reverse('tercero:empr_borrar', args=(self.pk,))

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresaes'
        ordering = ['razon_social']
