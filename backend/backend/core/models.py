from django.db import models
import uuid


class UuidModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        unique=True,
        editable=False,
        default=uuid.uuid4
    )

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    criado_em = models.DateTimeField(
        'Criado em',
        auto_now_add=True
    )
    modificado_em = models.DateTimeField(
        'Modificado em',
        auto_now=True
    )

    class Meta:
        abstract = True


# class CreateAt(models.Model):
#     criado_por = models.ForeignKey(
#         User,
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#         default=1
#     )

#     class Meta:
#         abstract = True


class IsActive(models.Model):
    active = models.BooleanField(
        'Active',
        default=True
    )

    class Meta:
        abstract = True


class DefaultInerance(UuidModel, TimeStampedModel, IsActive):
    class Meta:
        abstract = True
