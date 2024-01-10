from rest_framework import serializers
from .models import Motoboy


class MotoboySerializer(serializers.ModelSerializer):

    class Meta:
        model = Motoboy
        fields = '__all__'
