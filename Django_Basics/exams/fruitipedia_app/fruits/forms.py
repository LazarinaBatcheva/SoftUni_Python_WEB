from django import forms
from fruitipedia_app.mixins import NoLabelsMixin, DisabledFieldMixin
from fruits.models import Fruit


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        exclude = ['owner']


class FruitAddForm(NoLabelsMixin, FruitBaseForm):
    class Meta(FruitBaseForm.Meta):
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Fruit Image URL'}),
            'description': forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
            'nutrition': forms.Textarea(attrs={'placeholder': 'Nutrition Info'}),
        }


class FruitEditForm(FruitBaseForm):
    pass


class FruitDeleteForm(DisabledFieldMixin, FruitBaseForm):
    class Meta(FruitBaseForm.Meta):
        exclude = ['owner', 'nutrition']