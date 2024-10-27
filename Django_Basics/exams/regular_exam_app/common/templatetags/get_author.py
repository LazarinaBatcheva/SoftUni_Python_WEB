from django import template
from regular_exam_app.utils import get_author_obj


register = template.Library()


@register.simple_tag
def get_author():
    return get_author_obj()