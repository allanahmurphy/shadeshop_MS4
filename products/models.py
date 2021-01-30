from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator

from profiles.models import UserProfile


class Brand(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    brand = models.ForeignKey('Brand', null=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sale = models.BooleanField()
    saleprice = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_credit = models.CharField(max_length=254, null=True, blank=True)

    def clean(self):
        if self.sale and self.saleprice is None:
            raise ValidationError("Sale items must have sale price")

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE, related_name='review')
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=False, blank=False, related_name='review')
    description = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
