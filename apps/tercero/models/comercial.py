from django.urls import reverse
from django.db import models

from apps.comunes.models import AudtoriaMixin, Domicilio, Comunicacion
from apps.persona.models import Persona

class Comercial(AudtoriaMixin):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    domicilios = models.ManyToManyField(Domicilio, related_name='comercial_domicilios', blank=True)
    comunicaciones = models.ManyToManyField(Comunicacion, related_name='comercial_comunicaciones', blank=True)

    def __str__(self):
        if self.persona.apellido is None:
            return "-"
        else:
            return "%s %s" % (self.persona.nombre, self.persona.apellido)

    def get_absolute_url(self):
        # reverse('persona:info', kwargs={'pk': self.pk})
        return reverse('tercero:come_info', args=(self.pk,))

    def get_update_url(self):
        return reverse('tercero:come_modif', args=(self.pk,))

    def get_delete_url(self):
        return reverse('tercero:come_borrar', args=(self.pk,))

    class Meta:
        verbose_name = 'Comercial'
        verbose_name_plural = 'Comerciales'
        ordering = ['persona__nombre', 'persona__apellido']
