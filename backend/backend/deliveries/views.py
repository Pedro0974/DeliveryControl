from rest_framework import generics, filters
from .models import (
    PaymentMethod,
    DeliveryFee,
    Delivery
)
from .serializers import (
    PaymentMethodSerializer,
    DeliveryFeeSerializer,
    DeliverySerializer
)


class PaymentMethodFilters(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        name = request.query_params.get('name', None)

        filters = {}

        if name:
            filters['name__icontains'] = name

        return queryset.filter(**filters)


class PaymentMethodListCreateAPIView(generics.ListCreateAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    filter_backends = [PaymentMethodFilters]


class PaymentMethodRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer


class DeliveryFeeFilters(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        price = request.query_params.get('price', None)

        filters = {}

        if price:
            filters['price__icontains'] = price

        return queryset.filter(**filters)


class DeliveryFeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = DeliveryFee.objects.all()
    serializer_class = DeliveryFeeSerializer
    filter_backends = [DeliveryFeeFilters]


class DeliveryFeeRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = DeliveryFee.objects.all()
    serializer_class = DeliveryFeeSerializer


class DeliveryFilters(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        price = request.query_params.get('price', None)
        motoboy_name = request.query_params.get('motoboy_name', None)
        date = request.query_params.get('date', None)
        status = request.query_params.get('status', None)
        paymant_method_name = request.query_params.get(
            'paymant_method_name', None)

        filters = {}

        if price:
            filters['price'] = price

        if motoboy_name:
            filters['motoboy_name__name__icontains'] = motoboy_name

        if date:
            filters['date'] = date

        if status:
            filters['status'] = status

        if paymant_method_name:
            filters['paymant_method-_name__icontains'] = paymant_method_name

        return queryset.filter(**filters)


class DeliveryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    filter_backends = [DeliveryFilters]


class DeliveryRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
