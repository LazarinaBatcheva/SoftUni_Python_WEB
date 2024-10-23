from django import template
from exam_prep.utils import get_profile_obj


register = template.Library()


@register.simple_tag
def get_profile():
    return get_profile_obj()
