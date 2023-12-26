from rest_framework import serializers

from apps.course.models import Course, CourseDepartment, CourseAuthor, CourseVideo, CourseComment, CoursePayment, CourseSubscription


class CourseMainSerializer(serializers.ModelSerializer):
    department_count = serializers.IntegerField(default=0)
    category = serializers.SlugRelatedField(
        read_only=True, many=False, slug_field='title')
    author = serializers.SlugRelatedField(
        read_only=True, many=False, slug_field='title')

    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'pic',
            'author',
            'lang',
            'level',
            'rating',
            'dis_price',
            'price',
            'department_count',
            'category',
        ]


class CourseVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseVideo
        fields = [
            'id',
            # 'department',
            'title',
            'thumbnail',
            'video',
            'video_length',
            'content',
        ]


class CourseDepartmentSerializer(serializers.ModelSerializer):
    videos = CourseVideoSerializer(many=True)

    class Meta:
        model = CourseDepartment
        fields = [
            'id',
            # 'course',
            'title',
            'videos',
        ]


class CourseGetCommentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, many=False, slug_field='full_name')

    class Meta:
        model = CourseComment
        fields = [
            'id',
            'user',
            'content',
            'created_at',

        ]

# class CourseCommentSerializer(serializers.ModelSerializer)


class CourseSubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSubscription
        fields = [
            'id',
            'course',
            'user',
            'is_subscribe',
        ]


class CourseDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        read_only=True, many=False, slug_field='title')
    author = serializers.SlugRelatedField(
        read_only=True, many=False, slug_field='title')
    departments = CourseDepartmentSerializer(many=True)
    # comments = CourseGetCommentSerializer(many=True)

    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'pic',
            'author',
            'lang',
            'level',
            'rating',
            'dis_price',
            'price',
            'category',
            'departments',
            # 'comments',
        ]
