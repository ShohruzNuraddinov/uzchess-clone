from django.urls import path

from apps.library.views import BookListAPIView, BookRetrieveAPIView


urlpatterns = [
    path('', BookListAPIView.as_view()),
    path('book/<int:pk>/', BookRetrieveAPIView.as_view())
]
