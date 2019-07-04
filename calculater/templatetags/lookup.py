from django import template
register = template.Library()


@register.filter(name='lookup')
def lookup(value, arg, default=""):
    if arg in value:
        return round(value[arg])
    else:
        return default
