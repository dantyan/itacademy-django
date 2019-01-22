from django.core import validators
from django.db import models


class TestUser(models.Model):
    email = models.EmailField()
    password = models.CharField(
        max_length=16,
        validators=[
            validators.MaxLengthValidator(16),
            validators.MinLengthValidator(3)
        ]
    )
    join_date = models.DateField(auto_now_add=True)
    username = models.CharField(
        max_length=16,
        validators=[
            validators.MaxLengthValidator(16),
            validators.MinLengthValidator(8)
        ]
    )
    is_active = models.BooleanField(default=False)
    company = models.CharField(
        max_length=256,
        null=True,
        blank=True
    )
