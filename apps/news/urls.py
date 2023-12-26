from django.urls import path

from apps.news.views import NewsListAPIView, NewsRetrieveAPIView, NewsVisitorCreateAPIView

urlpatterns = [
    path('', NewsListAPIView.as_view()),
    path('<int:pk>/', NewsRetrieveAPIView.as_view()),
    path('visitor/add/', NewsVisitorCreateAPIView.as_view())
]
