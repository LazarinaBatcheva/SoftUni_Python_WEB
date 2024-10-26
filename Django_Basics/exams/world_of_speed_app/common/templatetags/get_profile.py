from django import template
from world_of_speed_app.utils import get_profile_obj


register = template.Library()


@register.simple_tag
def get_profile():
    return get_profile_obj()