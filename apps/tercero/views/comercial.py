from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q

from apps.comunes.models import Domicilio, Comunicacion

from apps.tercero import forms
from apps.tercero import models

PAGINATION = 15


class listado(ListView):
    model = forms.Comercial
    template_name = 'comercial/listado.html'
    paginate_by = PAGINATION


class nuevo(CreateView):
    model = models.Comercial
    template_name = 'comercial/formulario.html'
    form_class = forms.ComercialForm

    def get_success_url(self):
        return reverse_lazy('tercero:come_listado')


class detalle(DetailView):
    model = models.Comercial
    template_name = 'comercial/info.html'

    def get_context_data(self, **kwargs):
        context = super(detalle, self).get_context_data(**kwargs)
        context['domicilios'] = context['comercial'].domicilios.filter(active=True)
        context['comunicaciones'] = context['comercial'].comunicaciones.filter(active=True)
        return context

class modificacion(UpdateView):
    model = models.Comercial
    template_name = 'comercial/formulario.html'
    form_class = forms.ComercialForm


class eliminacion(DeleteView):
    model = models.Comercial

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('tercero:come_listado')