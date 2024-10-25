from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class OnlyLettersValidator:
    def __init__(self, message=None):
        self.message = message or 'Fruit name should contain only letters!'

    def __call__(self, value: str):
        if not value.isalpha():
            raise ValidationError(self.message)