from rest_framework import serializers

from apps.news.models import News, NewsVisitor


class NewsSerialzier(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            'id',
            'image',
            'title',
            'sub_title',
            'content',
            'view_count'
        ]


class NewsVisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsVisitor
        fields = [
            'id',
            'news',
            'visitor_key'
        ]
