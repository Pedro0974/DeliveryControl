from rest_framework import generics, filters
from .models import Motoboy
from .serializers import MotoboySerializer
# from django.db.models import Q


class MotoboyFilters(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        name = request.query_params.get('name', None)
        age = request.query_params.get('age', None)
        phone = request.query_params.get('phone', None)

        filters = {}

        if name:
            filters['name__icontains'] = name

        if age:
            filters['age'] = age

        if phone:
            filters['phone__icontains'] = phone

        return queryset.filter(**filters)


class MotoboyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Motoboy.objects.all()
    serializer_class = MotoboySerializer
    filter_backends = [MotoboyFilters]


class MotoboyRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Motoboy.objects.all()
    serializer_class = MotoboySerializer
