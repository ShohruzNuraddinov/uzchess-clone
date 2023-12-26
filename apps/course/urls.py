from django.urls import path

from apps.course.views import CourseListAPIView, CourseRetrieveAPIView, CourseCommentsListAPIView, IsSubscribeCourseView

urlpatterns = [
    path('', CourseListAPIView.as_view()),
    path('<int:pk>/', CourseRetrieveAPIView.as_view()),
    path('<int:course_id>/comments/', CourseCommentsListAPIView.as_view()),
    # path('subscribe/', CourseSubscribeCreateAPIView.as_view()),
    path('is_subscribe/<int:course_id>/', IsSubscribeCourseView.as_view()),
]
