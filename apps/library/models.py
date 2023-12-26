from django.db import models
from django.conf import settings

from apps.utils.models import BaseModel
from apps.library.choices import BookTextChoices
# Create your models here.


class BookCategory(BaseModel):
    title = models.CharField(max_length=256)

    pic = models.ImageField(upload_to='book/category/pic/', blank=True, null=True)

    

class BookAuthor(BaseModel):
    name = models.CharField(max_length=256)


class Book(BaseModel):
    title = models.CharField(max_length=256)
    about = models.TextField()

    dis_price = models.FloatField()
    price = models.FloatField()

    rating = models.FloatField(default=0)

    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    author = models.ForeignKey(BookAuthor, on_delete=models.CASCADE)

    level = models.CharField(max_length=128, choices=BookTextChoices.choices)
    lang = models.CharField(max_length=128, choices=settings.LANGUAGES)

    pic = models.ImageField(upload_to='book/pic/', blank=True, null=True)

    published_at = models.IntegerField()
    page_count = models.IntegerField()

    orders_count = models.IntegerField(default=0)
