from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.TextField()
    bio = models.TextField(blank=True, null=True)
    verifiedReviewer = models.BooleanField(default=False)

