from backend.core.models import DefaultInerance
from django.db import models


class Motoboy(DefaultInerance):
    name = models.CharField(
        'Name',
        max_length=255,
        blank=False,
        null=False
    )
    age = models.IntegerField(
        'Age',
        blank=False,
        null=False
    )
    phone = models.CharField(
        'Phone',
        max_length=12,
        blank=False,
        null=False
    )

    class Meta:
        ordering = ('name', )
        verbose_name = 'Motoboy'
        verbose_name_plural = 'Motoboys'

    def __str__(self):
        return f'{self.name} - {self.phone}'
