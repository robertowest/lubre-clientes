import os

from django.conf import settings


# -------------------------
# aplicaciones del proyecto
# -------------------------
settings.INSTALLED_APPS += [
    'apps.home',
    'apps.comunes',
    'apps.persona',
    'apps.tercero',
]


# -------------
# base de datos
# -------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lubre_dev',
        'USER': 'roberto',
        'PASSWORD': 'roberto',
        'HOST': '192.168.1.2',
        'PORT': '3306',
    }
}


# ---------------
# host permitidos
# ---------------
ALLOWED_HOSTS = ['*']


# ---------------
# internalización
# ---------------
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Argentina/Tucuman'


# --------------------------------
# configuración para la contraseña
# --------------------------------
settings.AUTH_PASSWORD_VALIDATORS = [
]


# -----------------------------------
# ubicación de los templates públicos
# -----------------------------------
settings.TEMPLATES[0]['DIRS'] = [
    os.path.join(settings.BASE_DIR, "templates"),
]


# ------------------
# archivos estáticos
# ------------------
STATIC_URL = '/statics/'
STATICFILES_DIRS = [os.path.join(settings.BASE_DIR, 'statics'), ]


# ----------------
# archivos subidos
# ----------------
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(settings.BASE_DIR, 'media')


# ------------
# traducciones
# ------------
LOCALE_PATHS = [os.path.join(settings.BASE_DIR, 'locale'),]


# --------------------------------------
# agregar contenido a context_processors
# --------------------------------------
# settings.TEMPLATES[0]['OPTIONS']['context_processors'].append('social_django.context_processors.backends')


# ------------------------------------------------------
# aplicaciones de terceros, middleware y configuraciones
# ------------------------------------------------------
settings.INSTALLED_APPS += [
    'debug_toolbar',
    'django_filters',
    'material',
]

settings.MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',  # debug
]

INTERNAL_IPS = ['localhost', '127.0.0.1', '172.19.0.1', '172.20.0.1']  # debug (gateway del docker)


# ---------------------------------------------
# configucaciones para aplicaciones de terceros
# ---------------------------------------------
# debug
INTERNAL_IPS = ['localhost', '127.0.0.1', '172.19.0.1']  # gateway del docker


# -----------------------------
# redireccionamiento para login
# -----------------------------
LOGIN_URL = '/usuario/login/'
LOGIN_REDIRECT_URL = '/'

LOGOUT_URL = '/usuario/logout/'
LOGOUT_REDIRECT_URL = '/'


# para que funcione el proceso de registro de usuarios
# esto evitará que se envíe un email e imprimirá el resultado por la consola
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = os.path.join(settings.BASE_DIR, "sent_emails")