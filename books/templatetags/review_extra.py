from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')


# on not using the 'name' argument django automat using the func name
@register.filter
@stringfilter  # used for template tags tha only expect strings
def lower(value):
    return value.lower()


# is_safe option automatically escapes input values gives safe strings
@register.filter(is_safe=True)
def mysafefilter(value):
    return value
