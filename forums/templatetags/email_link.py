from django import template

register = template.Library()

@register.simple_tag
def email_link(email):
    return '<a href="mailto://%s">%s</a>' % (email, email)
    
@register.filter
def uppercase(value):
    return value.upper()