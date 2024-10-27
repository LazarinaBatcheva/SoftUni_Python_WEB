from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class OnlyLettersValidator:
    def __init__(self, message=None):
        self.message = message or 'Your name must contain letters only!'

    def __call__(self, value: str):
        if not value.isalpha():
            raise ValidationError(self.message)


@deconstructible
class OnlyDigitsValidator:
    def __init__(self, message=None):
        self.message = message or 'Your passcode must be exactly 6 digits!'

    def __call__(self, value: str):
        if not value.isdigit() or len(value) != 6:
            raise ValidationError(self.message)
