from django.db import models
from django.conf import settings

from social_media_api.accounts.models import User  # to get the custom user model

class Post(models.Model):
    title = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

class Link(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='likes')


class Notification(models.Model):
    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notifications"
    )
    actor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notifications_sent"
    )
    verb = models.CharField(max_length=255) 
    
    # Generic relation to any object (post, comment, etc.)
    target_content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    target_object_id = models.PositiveIntegerField(blank=True, null=True)
    target = GenericForeignKey("target_content_type", "target_object_id")

    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)  # Optional: track if seen

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return f"{self.actor} {self.verb} {self.target} → {self.recipient}"    