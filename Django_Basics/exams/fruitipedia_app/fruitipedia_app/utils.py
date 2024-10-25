from profiles.models import Profile


def get_profile_obj():
    return Profile.objects.first()