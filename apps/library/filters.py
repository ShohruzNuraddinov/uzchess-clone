from django_filters import rest_framework as filters

from apps.library.models import Book


class BookFilterSet(filters.FilterSet):
    rating = filters.NumberFilter(field_name='rating', lookup_expr='gte')

    class Meta:
        model = Book
        fields = [
            'lang',
            'level',
            'category',
            'rating'
        ]
