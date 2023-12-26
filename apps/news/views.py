from rest_framework import generics
from rest_framework import filters

from apps.news.models import News, NewsVisitor
from apps.news.serializers import NewsSerialzier, NewsVisitorSerializer

# Create your views here.


class NewsListAPIView(generics.ListAPIView):
    serializer_class = NewsSerialzier
    queryset = News.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ["title"]


class NewsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = NewsSerialzier
    queryset = News.objects.all()


class NewsVisitorCreateAPIView(generics.CreateAPIView):
    serializer_class = NewsVisitorSerializer
    queryset = NewsVisitor.objects.all()
