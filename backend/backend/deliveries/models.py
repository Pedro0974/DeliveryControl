from backend.core.models import DefaultInerance
from backend.motoboys.models import Motoboy
from django.db import models


STATUS_CHOICES = [
    ('CREDITO', 'Credito'),
    ('DEBITO', 'Debito'),
    ('DINHEIRO', 'Dinheiro'),
    ('PIX', 'Pix'),
    ('PAGAMENTO ONLINE', 'Pagamento Online')
]


class PaymentMethod(DefaultInerance):
    name = models.CharField(
        'Name',
        max_length=255,
        blank=False,
        null=False
    )

    class Meta:
        ordering = ('name', )
        verbose_name = 'Payment Method'
        verbose_name_plural = 'Payment Methods'

    def __str__(self):
        return f'{self.name}'


class DeliveryFee(DefaultInerance):
    price = models.FloatField(
        'Price',
    )

    class Meta:
        ordering = ('price', )
        verbose_name = 'Delivery Fee'
        verbose_name_plural = 'Delivery Fees'

    def __str__(self):
        return f'{self.price}'


class Delivery(DefaultInerance):
    motoboy_id = models.ForeignKey(
        Motoboy,
        on_delete=models.DO_NOTHING,
        blank=False,
        null=False
    )
    date = models.DateTimeField(
        'Date',
        auto_now_add=True
    )
    price = models.FloatField(
        'Price',
    )
    delivery_fee_id = models.ForeignKey(
        DeliveryFee,
        on_delete=models.DO_NOTHING,
        blank=False,
        null=False
    )
    payment_method_id = models.ForeignKey(
        PaymentMethod,
        on_delete=models.DO_NOTHING,
        blank=False,
        null=False
    )
    status = models.CharField(
        'Status',
        max_length=50,
        choices=STATUS_CHOICES,
        blank=False,
        null=False
    )

    class Meta:
        ordering = ('date', )
        verbose_name = 'Delivery'
        verbose_name_plural = 'Deliveries'

    def __str__(self):
        return f'{self.date} - {self.motoboy_id} - {self.price}'
