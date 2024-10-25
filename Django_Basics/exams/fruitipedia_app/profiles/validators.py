import re
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class StartWithLetterValidator:
    def __init__(self, message=None):
        self.message = message or 'Your name must start with a letter!'

    def __call__(self, value: str):
        if not re.match(r'^[A-Za-z]', value):
            raise ValidationError(self.message)