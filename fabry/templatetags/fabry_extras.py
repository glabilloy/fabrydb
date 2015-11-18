from django import template
from django.conf import settings

register = template.Library()

@register.inclusion_tag('site/mailto_support.html')
def mailto_support():
    return  {"support_email": settings.SUPPORT_EMAIL }
