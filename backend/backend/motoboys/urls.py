from django.urls import path
from .views import (
    MotoboyListCreateAPIView,
    MotoboyRetrieveUpdateAPIView
)

urlpatterns = [
    path(
        'motoboy',
        MotoboyListCreateAPIView.as_view(),
        name='motoboy-list-create-api-view'
    ),
    path(
        'motoboy/<str:pk>/',
        MotoboyRetrieveUpdateAPIView.as_view(),
        name='motoboy-retrieve-update-api-view'
    ),
]
