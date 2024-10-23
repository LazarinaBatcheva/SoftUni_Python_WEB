from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from profiles.vallidators import AlphaNumericValidator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            AlphaNumericValidator(),
        ],
    )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
