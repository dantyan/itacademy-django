import uuid

from django.core import validators
from django.db import models


def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = "{}.{}".format(uuid.uuid4(), ext.lower())
    return f'testuser/{filename}'


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
            validators.MinLengthValidator(6)
        ]
    )
    is_active = models.BooleanField(default=False)
    company = models.CharField(
        max_length=256,
        null=True,
        blank=True
    )
    birth_date = models.DateField(
        'День варенья',
        null=True,
        blank=True
    )

    avatar = models.ImageField(
        upload_to=upload_to,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.username
