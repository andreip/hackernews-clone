import urlparse

from django import template

register = template.Library()


@register.filter
def domain(url):
    try:
        return urlparse.urlparse(url).netloc
    except:
        return ''
