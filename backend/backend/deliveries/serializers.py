from rest_framework import serializers
from .models import (
    PaymentMethod,
    DeliveryFee,
    Delivery
)


class PaymentMethodSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentMethod
        fields = '__all__'


class DeliveryFeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeliveryFee
        fields = '__all__'


class DeliverySerializer(serializers.ModelSerializer):
    paymant_method_id = PaymentMethodSerializer()
    delivery_fee_id = DeliveryFeeSerializer()

    class Meta:
        model = Delivery
        fields = '__all__'
