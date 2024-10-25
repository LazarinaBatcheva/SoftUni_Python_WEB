from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class CarYearValidator:
    def __init__(self, start_year: int, end_year: int, message=None):
        self.start_year = start_year
        self.end_year = end_year
        self.message = message or f'Year must be between {self.start_year} and {self.end_year}!'

    def __call__(self, value: int):
        if value < self.start_year or value > self.end_year:
            raise ValidationError(self.message)
