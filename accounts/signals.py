from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from webapp.models import Post


@receiver(signal=post_save, sender=Post)
def add_user_post(sender, instance, created, **kwargs):
    if created:
        user = get_user_model().objects.get(pk=instance.author.id)
        user.posts_total += 1
        user.save()
