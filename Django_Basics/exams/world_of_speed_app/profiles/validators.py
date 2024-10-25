from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.text import slugify


@deconstructible
class AlphaNumericValidator:
    def __init__(self, message=None):
        self.message = message or 'Username must contain only letters, digits, and underscores!'

    def __call__(self, value: str):
        if (value.lower() != slugify(value) or '-' in value) and not any(char.isalnum() for char in value):
            raise ValidationError(self.message)