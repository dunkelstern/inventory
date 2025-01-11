from django import template
from django.utils.safestring import mark_safe
from django.utils.formats import number_format

from inventory.models import Settings

register = template.Library()
s = None

@register.filter(name='currency')
def currency(value, format):
    global s
    if s is None:
        s = Settings.objects.first()
    value = float(value)

    if format == 'detail':
        value = number_format(round(value, 3), 3, use_l10n=True)
    else:
        value = number_format(round(value, 2), 2, use_l10n=True)

    if format == 'long' or format == 'detail':
        symbol = s.currency
    else:
        symbol = s.currency_symbol
    
    if s.currency_symbol_position:
        result = f"{value} {symbol}"
    else:
        result = f"{symbol} {value}"

    return mark_safe(result)