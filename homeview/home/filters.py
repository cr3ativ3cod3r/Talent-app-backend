# filters.py
import django_filters
from .models import Item
from django.contrib.auth.models import User


class SearchFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(field_name='username', lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['username']

class ItemFilter(django_filters.FilterSet):
    time = django_filters.CharFilter(field_name='time')

    class Meta:
        model = Item
        fields = ['time']
