from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(
        blank=True, null=True, upload_to='uploads', default='uploads/avatar.jpg'
    )
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
