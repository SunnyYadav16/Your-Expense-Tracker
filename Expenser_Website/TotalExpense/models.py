from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Expense(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=10)
    description = models.TextField()
    date = models.DateField(default=now)
    category = models.CharField(max_length=266)

    def __str__(self):
        return self.category


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
