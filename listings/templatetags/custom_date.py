from django import template
from django.utils import formats
import datetime
register = template.Library()


@register.filter(expects_localtime=True, is_safe=False)
def custom_date(value):
    m = {
        "01": "Jan.",
        "02": "Feb.",
        "03": "Mar.",
        "04": "Apr.",
        "05": "May",
        "06": "Jun.",
        "07": "Jul.",
        "08": "Aug.",
        "09": "Sep.",
        "10": "Oct.",
        "11": "Nov.",
        "12": "Dec.",
    }
    if value in (None, ''):
        return ''

    if isinstance(value, str):
       
        if 'Z' in value:
            value = m[value[5:7]] + " " + value[8:10] + ", " + value[0:4]    
        else:
            value = "N/A"

    try:
        return formats.date_format(value)
    except AttributeError:
        try:
            return format(value)
        except AttributeError:
            return ''
