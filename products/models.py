from django.db import models

class Brand(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.CharField(max_length=255)
    product_url = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    nicotine_content = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
    npk = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        npk = (self.size * self.nicotine_content) / self.price
        round_npk = round(npk, 2)
        self.npk = round_npk
        super(Product, self).save(*args, **kwargs)