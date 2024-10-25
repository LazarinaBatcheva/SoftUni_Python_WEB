from fruitipedia_app.utils import get_profile_obj


class PlaceholderMixin:
    def add_placeholder_with_field_name(self):
        for field_name, field in self.fields.items():
            placeholder = field_name.replace('_', ' ').capitalize()
            field.widget.attrs['placeholder'] = placeholder

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_placeholder_with_field_name()


class NoLabelsMixin:
    def remove_labels(self):
        for field in self.fields.values():
            field.label = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.remove_labels()


class DisabledFieldMixin:
    def disabled_fields(self):
        for field in self.fields.values():
            field.disabled = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disabled_fields()
