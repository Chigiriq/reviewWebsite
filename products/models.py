from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/")
    price = models.PositiveIntegerField(null=True, blank=True)

    description = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})
