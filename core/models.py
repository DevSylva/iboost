from django.db import models
from account.models import User

# Create your models here.
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    charge = models.FloatField()
    post_balance = models.FloatField()


    def __str__(self):
        return self.user


class DepositLog(models.Model):
    GATEWAY = (
        ("FLUTTERWAVE", "FLUTTERWAVE"),
        ("COINBASE", "COINBASE"),
        ("BANK", "BANK"),
    )
    STATUS = (
        ("PENDING", "PENDING"),
        ("COMPLETED", "COMPLETED"),
    )

    dateway = models.CharField(max_length=30)
    status = models.CharField(choices=STATUS, default=STATUS[0], max_length=30)
    time = models.DateTimeField()

class Order(models.Model):
    STATUS = (
        ("PENDING", "PENDING"),
        ("COMPLETED", "COMPLETED"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.CharField(max_length=30)
    link = models.URLField()
    quantity = models.PositiveIntegerField()
    status = models.CharField(choices=STATUS, default=STATUS[0], max_length=30)