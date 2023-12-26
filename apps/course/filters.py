from django_filters import rest_framework as filters

from apps.course.models import Course


class CourseFilterSet(filters.FilterSet):
    rating = filters.NumberFilter(field_name='rating', lookup_expr='gte')

    class Meta:
        model = Course
        fields = [
            'level',
            'category',
            'lang',
            'rating',
        ]
