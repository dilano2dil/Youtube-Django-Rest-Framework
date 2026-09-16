from django.db import models
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('api:product_api_detail', kwargs={'pk': self.pk})

    def price_in_dollars(self):
        return f"{self.price:.2f} $"

    def __str__(self):
        return self.name