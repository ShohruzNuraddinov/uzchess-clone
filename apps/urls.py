from django.urls import path, include


urlpatterns = [
    path('auth/', include('apps.user.urls')),
    path('news/', include('apps.news.urls')),
    path('course/', include('apps.course.urls')),
    path('library/', include('apps.library.urls'))
]
