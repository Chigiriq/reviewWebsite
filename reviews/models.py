from django.db import models
from django.conf import settings
from django.urls import reverse

class Review(models.Model):
    title = models.CharField(max_length=255)
    game = models.CharField(max_length=30, blank=True, null=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("review_detail", kwargs={"pk": self.pk})
    
class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse("review_list")