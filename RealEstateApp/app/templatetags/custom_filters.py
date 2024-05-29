from django import template

register = template.Library()

@register.filter(name="split_decimal")
def split_deciaml(value):
    interger_part = int(value)
    decimal_part = round(value-interger_part,2)
    return interger_part, decimal_part

@register.filter(name='make_range') 
def make_range(number):
    if(number[1] != 0.5):
       return range(number[0]), range(5-number[0]), False
    else:
        if(number[0] != 0):
            return range(number[0]), range(5-number[0]-1), True
        else:
            return range(number[0]), range(5-number[0]), False

@register.filter(name='empty_stars') 
def empty_stars(number):
    return range(5 - number)