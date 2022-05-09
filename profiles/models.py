from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    displayName = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    photoSrc = models.ImageField(upload_to="profile-pictures", null=True, blank=True)
    date_joined = models.DateTimeField(blank=True, null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.user = None

    def __str__(self):
        return str(self.user)



class Follower(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner'
    )
    subscriber = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscribers'
    )
