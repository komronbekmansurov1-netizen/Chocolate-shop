from django.db import models

# Create your models here.
class ChocolateProduct(models.Model):
    class Existence(models.TextChoices):
        HAVE = 'have got', 'Bor'
        NOT_HAVE = "have_not_got", "Yo'q"
    class ProductType(models.TextChoices):
        DARK = 'dark', 'Dark'
        MILK = 'milk', 'Milk'
        WHITE = 'white', 'White'
        ICE_CREAM = 'ice_cream', 'Ice Cream'
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.PositiveIntegerField(default=0)
    existence = models.CharField(max_length=100, choices=Existence.choices)
    product_type = models.CharField(max_length=100, choices=ProductType.choices)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    chocolate_product = models.ForeignKey(ChocolateProduct, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name