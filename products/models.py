from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.CharField(max_length=255)
    product_url = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    nicotine_content = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title