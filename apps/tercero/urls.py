from django.urls import path

from apps.tercero.views import comercial, empresa

app_name = 'tercero'

urlpatterns = [
    # comerciales
    path('comercial/', comercial.listado.as_view(), name='come_listado'),
    path('comercial/nuevo/', comercial.nuevo.as_view(), name='come_nuevo'),
    path('comercial/info/<int:pk>/', comercial.detalle.as_view(), name='come_info'),
    path('comercial/modif/<int:pk>/', comercial.modificacion.as_view(), name='come_modif'),
    path('comercial/borrar/<int:pk>/', comercial.eliminacion.as_view(), name='come_borrar'),

    # empresas
    path('empresa/', empresa.listado.as_view(), name='empr_listado'),
    path('empresa/nuevo/', empresa.nuevo.as_view(), name='empr_nuevo'),
    path('empresa/info/<int:pk>/', empresa.detalle.as_view(), name='empr_info'),
    path('empresa/modif/<int:pk>/', empresa.modificacion.as_view(), name='empr_modif'),
    path('empresa/borrar/<int:pk>/', empresa.eliminacion.as_view(), name='empr_borrar'),

    # empresas agrupadas
    path('empresa/actividad/', empresa.listado_actividad.as_view(), name='empr_acti_listado'),
]
