from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from apps.course.models import CoursePayment, CourseSubscription
from apps.course.choices import SUCCESS


@receiver(post_save, sender=CoursePayment)
def course_payment(sender, instance, created, **kwargs):
    if instance.status == SUCCESS:
        user = instance.user
        course = instance.course
        CourseSubscription.objects.create(
            user=user, course=course, is_subscribe=True
        )
