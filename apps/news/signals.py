from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.news.models import NewsVisitor


@receiver(post_save, sender=NewsVisitor)
def visitor_update(sender, instance, created, **kwargs):
    if created:
        instance.news.view_count += 1
        instance.news.save()
