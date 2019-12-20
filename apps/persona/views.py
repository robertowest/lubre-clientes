from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q

from . import forms
from . import models

PAGINATION = 15


class PersonaListView(ListView):
    model = forms.Persona
    template_name = 'persona/listado.html'
    paginate_by = PAGINATION

    def get_queryset(self, **kwargs):
        busqueda = self.request.GET.get('busqueda')
        if busqueda:
            result = models.Persona.objects.filter(
                Q(nombre__contains=busqueda) | Q(apellido__contains=busqueda)
            )
            # table.objects.filter(string__contains='a').filter(string__contains='b')
        else:
            result = models.Persona.objects.all()
        return result 


    # def get_queryset(self):
    #     filter_val = self.request.GET.get('filter', 'give-default-value')
    #     order = self.request.GET.get('orderby', 'give-default-value')
    #     new_context = models.Persona.objects.filter(nombre=filter_val,).order_by(order)
    #     return new_context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filter'] = self.request.GET.get('filter', 'give-default-value')
    #     context['orderby'] = self.request.GET.get('orderby', 'give-default-value')
    #     return context


class PersonaNewView(CreateView):
    model = models.Persona
    template_name = 'persona/formulario.html'
    form_class = forms.PersonaForm


class PersonaDetailView(DetailView):
    model = models.Persona
    template_name = 'persona/info.html'

    def post(self, request, *args, **kwargs):
        # comprobamos de dónde viene el post
        if request.path.find('info'):
            object = self.model.objects.get(pk=self.kwargs['pk'])
            object.delete()

        return redirect('persona:listado')


class PersonaUpdateView(UpdateView):
    model = models.Persona
    template_name = 'persona/formulario.html'
    form_class = forms.PersonaForm


class PersonaDeleteView(DeleteView):
    model = models.Persona
    # template_name = 'persona/confirmar_borrado.html'
    # success_url = reverse_lazy('persona:listado')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('persona:listado')
