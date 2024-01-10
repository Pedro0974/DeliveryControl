from django.urls import path
from .views import (
    PaymentMethodListCreateAPIView,
    PaymentMethodRetrieveUpdateAPIView,
    DeliveryFeeListCreateAPIView,
    DeliveryFeeRetrieveUpdateAPIView,
    DeliveryListCreateAPIView,
    DeliveryRetrieveUpdateAPIView
)

urlpatterns = [
    path(
        'paymant-method',
        PaymentMethodListCreateAPIView.as_view(),
        name='paymant-method-list-create-api-view'
    ),
    path(
        'paymant-method/<str:pk>/',
        PaymentMethodRetrieveUpdateAPIView.as_view(),
        name='paymant-method-retrieve-update-api-view'
    ),
    path(
        'delivery-fee',
        DeliveryFeeListCreateAPIView.as_view(),
        name='delivery-fee-list-create-api-view'
    ),
    path(
        'delivery-fee/<str:pk>/',
        DeliveryFeeRetrieveUpdateAPIView.as_view(),
        name='delivery-fee-retrieve-update-api-view'
    ),
    path(
        'delivery',
        DeliveryListCreateAPIView.as_view(),
        name='delivery-list-create-api-view'
    ),
    path(
        'delivery/<str:pk>/',
        DeliveryRetrieveUpdateAPIView.as_view(),
        name='delivery-retrieve-update-api-view'
    ),
]
