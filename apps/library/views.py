from rest_framework import generics, filters
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from apps.library.models import Book
from apps.library.filters import BookFilterSet
from apps.library.serializers import BookMainSerializer, BookDetailSerializer
# Create your views here.


class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all().select_related(
        'category',
        'author'
    )
    serializer_class = BookMainSerializer

    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title']
    filterset_class = BookFilterSet


class BookRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all().select_related(
        'category', 'author'
    )
    serializer_class = BookDetailSerializer
