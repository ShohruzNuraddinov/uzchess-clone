from django.db import models

class BookTextChoices(models.TextChoices):
    starter = "Starter"
    professional = "Professional"
    amateur = "Amateur"