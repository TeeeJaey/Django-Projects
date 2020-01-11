from django import template

register = template.Library()

@register.filter(name='replace')
def replace(value,arg):
    args = arg.split(',')
    arg1 = args[0]
    arg2 = args[1]
    return value.replace(arg1,arg2)
    