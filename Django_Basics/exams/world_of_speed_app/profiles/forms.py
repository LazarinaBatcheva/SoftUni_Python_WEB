from django import forms
from profiles.models import Profile
from world_of_speed_app.mixins import NoHelpTextMixin


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }


class ProfileCreateForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        exclude = ['first_name', 'last_name', 'profile_picture']


class ProfileEditForm(NoHelpTextMixin, ProfileBaseForm):
    help_text_fields = ['age']


class ProfileDeleteForm(ProfileBaseForm):
    pass
