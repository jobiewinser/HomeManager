import datetime
from django import template
register = template.Library()

@register.filter
def today_time_or_date(input_datetime):
    date = input_datetime.date()
    if date == datetime.date.today():
        return input_datetime.time()
    return date
    
    