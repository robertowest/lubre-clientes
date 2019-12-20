from django.urls import path
from . import views

app_name = 'persona'

urlpatterns = [
    path('', views.PersonaListView.as_view(), name='listado'),
    path('nuevo/', views.PersonaNewView.as_view(), name='nuevo'),
    path('info/<int:pk>/', views.PersonaDetailView.as_view(), name='info'),
    path('modif/<int:pk>/', views.PersonaUpdateView.as_view(), name='modif'),
    path('borrar/<int:pk>/', views.PersonaDeleteView.as_view(), name='borrar'),
]
