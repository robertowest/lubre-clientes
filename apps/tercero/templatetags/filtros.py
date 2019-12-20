from django import template

register = template.Library()


@register.filter
def filtro_active(modelo, valor):
    return modelo.filter(active=valor)


@register.filter
def query(qs, **kwargs):
    """ template tag which allows queryset filtering. Usage:
          {% query books author=author as mybooks %}
          {% for book in mybooks %}
            ...
          {% endfor %}
    """
    return qs.filter(**kwargs)
