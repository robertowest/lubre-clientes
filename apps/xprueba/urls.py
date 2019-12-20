from django.urls import include, path

from . import views

app_name = 'xprueba'

urlpatterns = [
    # listado filtrado mediante class-based
    path('', views.index),
    # listado filtrado mediante class-based view
    path('vista/', views.MyList.as_view(), name='MyList'),
    # CRUD con material.frontend
    path('crud/', include(views.MyCRUD().urls)),
]