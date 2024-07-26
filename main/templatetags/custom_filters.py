from django import template
from datetime import date

register = template.Library()

@register.filter
def calculate_age(dob):
    if not dob:
        return ''
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age


@register.filter(name='format_date_for_input')
def format_date_for_input(value):
    if value:
        return value.strftime('%Y-%m-%d')
    return ''


@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})