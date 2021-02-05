from django import template
from django.utils import formats
import datetime
register = template.Library()


@register.filter(expects_localtime=True, is_safe=False)
def custom_date(value, arg=None):
    if value in (None, ''):
        return ''

    if isinstance(value, str):
        api_date_format = '%Y-%m-%dT%H:%M:%S%z'  # 2019-08-30T08:22:32.245-0700
        api_date_format_2 = "%Y-%m-%d"
        if 'Z' in value:
            value = datetime.datetime.strptime(value, api_date_format)
        else:
            value = datetime.datetime.strptime(value, api_date_format_2)

    try:
        return formats.date_format(value, arg)
    except AttributeError:
        try:
            return format(value, arg)
        except AttributeError:
            return ''
