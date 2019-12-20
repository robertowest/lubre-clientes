from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django_filters.views import FilterView

from apps.tercero import forms
from apps.tercero import models
from apps.tercero import filters

PAGINATION = 15


class listado(FilterView):
    model = forms.Empresa
    template_name = 'empresa/listado_filtrado.html'
    filterset_class = filters.EmpresaFilter
    paginate_by = PAGINATION


class listado_ORG(ListView):
    model = forms.Empresa
    template_name = 'empresa/listado.html'
    paginate_by = PAGINATION
    form_class = forms.EmpresaFilter

    # para el filtro de información
    # def get_context_data(self, **kwargs):
    #     context = super(listado, self).get_context_data(**kwargs)
    #     context['comerciales'] = models.Comercial.objects.filter(active=True)
    #     return context
    def get_queryset(self):
        try:
            actividad = self.kwargs['actividad']
        except:
            # actividad = '1'
            actividad = ''

        if (actividad != ''):
            object_list = self.model.objects.filter(actividad_id=actividad)
        else:
            object_list = self.model.objects.all()
        return object_list        


class nuevo(CreateView):
    model = models.Empresa
    template_name = 'empresa/formulario.html'
    form_class = forms.EmpresaForm

    def get_context_data2(self, **kwargs):
        pass

    def get_success_url(self):
        return reverse_lazy('tercero:empr_listado')


class detalle(DetailView):
    model = models.Empresa
    template_name = 'empresa/info.html'

    def get_context_data(self, **kwargs):
        context = super(detalle, self).get_context_data(**kwargs)
        context['domicilios'] = context['empresa'].domicilios.filter(active=True)
        context['comunicaciones'] = context['empresa'].comunicaciones.filter(active=True)
        return context


class modificacion(UpdateView):
    model = models.Empresa
    template_name = 'empresa/formulario.html'
    form_class = forms.EmpresaForm


class eliminacion(DeleteView):
    model = models.Empresa

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('tercero:empr_listado')


from apps.comunes import models as mod2


class listado_actividad(ListView):
    model = mod2.Diccionario
    template_name = 'empresa/listado_agrupado.html'
    paginate_by = PAGINATION

    def get_context_data(self, **kwargs):
        context = super(listado_actividad, self).get_context_data(**kwargs)
        # context['empresas'] = models.Empresa.objects.filter(active=True)
        context['empresas'] = models.Empresa.objects.filter(nombre__istartswith='Agro')
        return context
