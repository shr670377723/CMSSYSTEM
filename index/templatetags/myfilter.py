#coding=utf-8
from django.template import Library
register = Library()
@register.filter
def date0(value):
    value = str(value)
    return value[:4]+'年'+value[4:6]+'月'