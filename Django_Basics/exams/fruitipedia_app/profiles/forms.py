from django import forms
from fruitipedia_app.mixins import PlaceholderMixin, NoLabelsMixin
from profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput()
        }


class ProfileCreateForm(PlaceholderMixin, NoLabelsMixin, ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        exclude = ['image_url', 'age']


class ProfileEditForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        exclude = ['email', 'password']


class ProfileDeleteForm(ProfileBaseForm):
    pass
