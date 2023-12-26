from django.shortcuts import get_object_or_404
from django.db import models
from rest_framework import generics
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from apps.course.models import Course, CourseComment, CourseSubscription
from apps.course.seriazliers import CourseMainSerializer, CourseDetailSerializer, CourseGetCommentSerializer, CourseSubscribeSerializer
from apps.course.filters import CourseFilterSet

# Create your views here.


class CourseListAPIView(generics.ListAPIView):
    serializer_class = CourseMainSerializer
    queryset = Course.objects.annotate(
        department_count=models.Count("departments")
    ).select_related('category', 'author')

    permission_classes = [AllowAny]

    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title']
    filterset_class = CourseFilterSet


class CourseRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all().prefetch_related(
        'departments__videos',
        'comments__user'
    )


class IsSubscribeCourseView(generics.GenericAPIView):
    serializer_class = CourseSubscribeSerializer
    queryset = CourseSubscription.objects.all()

    def get(self, request, course_id, *args, **kwargs):
        user = request.user
        data = {}
        queryset = self.get_queryset().filter(course_id=course_id, user=user)

        if not queryset.exists():
            data['is_subscribe'] = False
        data['is_subscribe'] = True

        return Response(data)
    



class CourseCommentsListAPIView(generics.ListAPIView):
    serializer_class = CourseGetCommentSerializer
    queryset = CourseComment.objects.all()
    permission_classes = [AllowAny]

    def filter_queryset(self, queryset):
        queryset = super(CourseCommentsListAPIView, self).filter_queryset(queryset)  # noqa
        return queryset.filter(course_id=self.kwargs["course_id"])
