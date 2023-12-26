from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        try:
            return self.title
        except Exception as error:
            return str(self.id)
