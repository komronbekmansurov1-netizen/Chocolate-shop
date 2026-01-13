from django.db import models
from users.models import User
# Create your models here.
class ProductReview(models.Model):
    Rating_choice = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    rating = models.CharField(max_length=100, choices=Rating_choice)

