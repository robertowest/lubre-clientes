"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # mis aplicaciones
    path('', include('apps.home.urls')),
    # comunes
    path('comunes/', include('apps.comunes.urls')),
    # otros
    path('usuario/', include('apps.usuario.urls')),
    path('persona/', include('apps.persona.urls')),
    # terceros
    path('tercero/', include('apps.tercero.urls')),

    # ejemplo y pruebas
    # path('prueba/', include('apps.xprueba.urls')),
]

from django.urls import include
from django.conf import settings

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]


from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
