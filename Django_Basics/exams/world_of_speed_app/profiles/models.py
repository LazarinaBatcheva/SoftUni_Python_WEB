from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from profiles.validators import AlphaNumericValidator


def get_name_field():
    return models.CharField(
        max_length=25,
        null=True,
        blank=True,
    )


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(
                3,
                'Username must be at least 3 chars long!'),
            AlphaNumericValidator(),
        ],
    )

    email = models.EmailField()

    age = models.IntegerField(
        validators=[
            MinValueValidator(21),
        ],
        help_text='Age requirement: 21 years and above.',
    )

    password = models.CharField(
        max_length=20,
    )

    first_name = get_name_field()

    last_name = get_name_field()

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return ''

