from django import template

register = template.Library()

@register.filter(name='lookup')
def lookup(value, arg, default=""):
    if arg in value and type(value[arg]) is int:
        return round(value[arg])
    elif arg in value and type(value[arg]) is str:
        return value[arg]        
    else:
        return default
