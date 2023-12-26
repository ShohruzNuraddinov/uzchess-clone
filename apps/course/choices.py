from django.db import models

PAYMENT = 'PAYMENT'
SUCCESS = 'SUCCESS'
CANCELED = 'CANCELED'


class CourseLevelChoices(models.TextChoices):
    starter = "Starter"
    professional = "Professional"
    amateur = "Amateur"


class CourseOrderStatus(models.TextChoices):
    PAYMENT = PAYMENT
    SUCCESS = SUCCESS
    CANCELED = CANCELED
