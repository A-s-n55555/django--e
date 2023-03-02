from django import template

register =template.Library()
@register.filter(name='cut')
# our custom filters
def cut(value,arg):
    """
    this cuts out all value of arg 
    """
    return value.replace(arg,'')

# register.filter('cut',cut)  #this is alternative to @register....