from rest_framework import serializers

from apps.library.models import Book, BookAuthor, BookCategory


class BookMainSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', many=False, read_only=True)  # noqa
    author = serializers.SlugRelatedField(slug_field='name', many=False, read_only=True)  # noqa

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'dis_price',
            'price',
            'rating',
            'lang',
            'pic',
            'level',
            'category',
            'author',
        ]


class BookDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', many=False, read_only=True)  # noqa
    author = serializers.SlugRelatedField(slug_field='name', many=False, read_only=True)  # noqa

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'dis_price',
            'price',
            'rating',
            'lang',
            'pic',
            'level',
            'category',
            'author',
            'published_at',
            'page_count',
            'about'
        ]
