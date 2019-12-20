from django.shortcuts import render

# Create your views here.
from .models import PruebaFilter
from apps.comunes.models import Localidad

def index(request):
    f = PruebaFilter(request.GET, queryset=Localidad.objects.all())
    return render(request, 'listado.html', {'filter': f})


from django_filters.views import FilterView
from .filters import MyFilter

class MyList(FilterView):
    model = Localidad
    template_name = 'listado2.html'
    filterset_class = MyFilter



from material.frontend.views import ModelViewSet

class LocalidadViewSet(ModelViewSet):
    model = Localidad
    ordering = ['nombre']
    list_display = ('nombre')