from django import template
from django.utils.safestring import mark_safe
from re import finditer

register = template.Library()


@register.filter(name='hilight')
def hilight(text, tokens):
    text = str(text)
    for token in tokens:
        ltext = text.lower()
        for token in tokens:
            positions = []
            for pos in finditer(token, ltext):
                positions.append(pos.start())
            if len(positions) > 0:
                offset = 0
                for pos in positions:
                    start = pos + offset
                    end = start + len(token)
                    text = text[:start] + f"<em>{text[start:end]}</em>" + text[end:]
                    offset += 9
    return mark_safe(text)
