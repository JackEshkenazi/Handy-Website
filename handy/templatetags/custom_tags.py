from django import template

register = template.Library()

@register.filter
def print_list(listy):

    if (isinstance(listy, list)):
    
        if (len(listy)==0):
            return "No listed cities"

        else:
            between = ", "
            return (between.join(listy))

    else:
        new_list=listy.split(">")
        
        for i in new_list:
            i.replace('<City: ', '')
            i.replace('>', '')

        return new_list


