from world_of_speed_app.utils import get_profile_obj


class ProfileObjectMixin:
    def get_object(self, queryset=None):
        return get_profile_obj()