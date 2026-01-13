from django.db import models
from users.models import User
from products.models import ChocolateProduct
# Create your models here.
class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Kutilmoqda'
        SHIPPED = 'shipped', "Jo'natildi"
        DELIVERED = 'delivered', "Yetkazib berildi"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateField()
    status = models.CharField(max_length=100, choices=Status.choices)
    total_price = models.PositiveIntegerField(default=0)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(ChocolateProduct, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    amount = models.IntegerField(default=0)
