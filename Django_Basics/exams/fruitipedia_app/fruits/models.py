from django.core.validators import MinLengthValidator
from django.db import models
from fruits.validators import OnlyLettersValidator


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2),
            OnlyLettersValidator(),
        ],
        unique=True,
        error_messages={
            'unique': 'This fruit name is already in use! Try a new one.',
        }
    )

    image_url = models.URLField()

    description = models.TextField()

    nutrition = models.TextField(
        null=True,
        blank=True,
    )

    owner = models.ForeignKey(
        to='profiles.Profile',
        on_delete=models.CASCADE,
        related_name='fruits',
    )
