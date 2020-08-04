from django import template

register = template.Library()

@register.simple_tag(name='formatstring')
def formatstring(value, *args):
    return value.format(*args)