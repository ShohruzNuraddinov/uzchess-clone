from django.db import models
from ckeditor.fields import RichTextField

from apps.utils.models import BaseModel
# Create your models here.


class News(BaseModel):
    image = models.ImageField(upload_to='media/news/', blank=True, null=True)
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    content = RichTextField()
    view_count = models.IntegerField(default=0)


class NewsVisitor(BaseModel):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='visitors')  # noqa
    visitor_key = models.CharField(max_length=32, unique=True)
