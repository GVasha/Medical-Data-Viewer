# viewer/templatetags/custom_tags.py

from django import template
import json
from django.utils.html import format_html

register = template.Library()

@register.filter
def attr(obj, attr_name):
    return getattr(obj, attr_name)

@register.filter
def call_method(obj, method_name):
    method = getattr(obj, method_name)
    if callable(method):
        return method()
    return method

@register.filter
def in_list(value, arg):
    return value in arg.split(',')

@register.simple_tag
def json_script(data, element_id):
    """
    Safely serialize data to JSON and wrap it in a <script> tag.
    """
    try:
        json_data = json.dumps(data)
    except TypeError:
        json_data = json.dumps({})
    return format_html(
        '<script type="application/json" id="{}">{}</script>',
        element_id,
        json_data
    )
