from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings

from apps.utils.models import BaseModel
from apps.user.models import User
from apps.course.choices import CourseLevelChoices, CourseOrderStatus
# Create your models here.


class Category(BaseModel):
    title = models.CharField(max_length=256)


class CourseAuthor(BaseModel):
    title = models.CharField(max_length=256)


class Course(BaseModel):
    title = models.CharField(max_length=256)

    pic = models.ImageField(
        upload_to='media/course/pic/', blank=True, null=True)

    lang = models.CharField(max_length=16, choices=settings.LANGUAGES)
    level = models.CharField(
        max_length=128, choices=CourseLevelChoices.choices)

    author = models.ForeignKey(CourseAuthor, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    dis_price = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    is_free = models.BooleanField(default=False)
    rating = models.FloatField(default=0)


class CourseDepartment(BaseModel):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='departments')

    title = models.CharField(max_length=256)



class CourseVideo(BaseModel):
    department = models.ForeignKey(
        CourseDepartment, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=256)
    thumbnail = models.ImageField(
        upload_to='media/course/videos/thumbnail/', blank=True, null=True)
    video = models.FileField(upload_to='media/course/videos/')
    video_duration = models.DurationField()

    content = RichTextField(blank=True, null=True)


class CourseComment(BaseModel):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    content = models.TextField()
    rating = models.FloatField(default=0)


class PaymentType(BaseModel):
    logo = models.ImageField(upload_to='media/payment/type/', blank=True, null=True)  # noqa
    title = models.CharField(max_length=128)


class CoursePayment(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    status = models.CharField(max_length=128, choices=CourseOrderStatus.choices)  # noqa
    price = models.FloatField()


class CourseSubscription(BaseModel):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='subscribe')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    is_subscribe = models.BooleanField(default=False)


class CourseUserView(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(
        CourseVideo, on_delete=models.CASCADE, related_name='user')

    last_watched_time = models.DurationField(blank=True, null=True)
    is_finished = models.BooleanField(default=False)
    percent = models.IntegerField(blank=True, null=True)
