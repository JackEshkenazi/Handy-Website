from django import template

register = template.Library()

@register.filter
def strip_list(list):
    between = ", "
    
    return (between.join(list))

register.filter('strip_list', strip_list)
