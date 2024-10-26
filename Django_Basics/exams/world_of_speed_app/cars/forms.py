from django import forms
from cars.models import Car
from world_of_speed_app.mixins import ReadOnlyMixin, DisabledFieldMixin


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['owner']
        widgets = {
            'image_url': forms.URLInput(
                attrs={'placeholder': 'https://...'}
            ),
        }


class CarAddForm(CarBaseForm):
    pass


class CarEditForm(CarBaseForm):
    pass


class CarDeleteForm(ReadOnlyMixin, DisabledFieldMixin, CarBaseForm):
    read_only_field = ['model', 'year', 'image_url', 'price']
    disabled_field = ['type']
