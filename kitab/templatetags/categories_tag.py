from django import template
from kitab.models import Category

register = template.Library()

@register.inclusion_tag('_nav.html')
def get_categories():
    categories = Category.objects.all()
    return {'categories':categories}


