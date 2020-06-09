from django import template

register = template.Library()

@register.filter
def print_list(list):

    if (len(list) == 0):
        return "No listed cities"

    else:
        between = ", "
        return (between.join(list))

