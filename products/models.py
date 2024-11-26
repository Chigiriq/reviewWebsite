from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
<<<<<<< HEAD
    image = models.ImageField(upload_to="images/", blank=True, null=True)
=======
    image = models.ImageField(upload_to="images/", null=True, blank=True)
>>>>>>> 251cee785c7b28a380996857f7c8a4bfdc42850a
    price = models.PositiveIntegerField(null=True, blank=True)

    description = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})
