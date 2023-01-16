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

    gateway = models.CharField(max_length=30)
    status = models.CharField(choices=STATUS, default=STATUS[0], max_length=30)
    time = models.DateTimeField()

class InstagramService(models.Model):

    SERVICE_NAME = (
        ("Real Nigerian Instagram Follower", "Real Nigerian Instagram Follower"),
        ("Instagram Reach + Impressions + Profile Visits [Post Link]", "Instagram Reach + Impressions + Profile Visits [Post Link]"),
        ("Instagram Reach + Impressions [Post Link]", "Instagram Reach + Impressions [Post Link]"),
        ("Instagram Emoji Comments", "Instagram Emoji Comments"),
        ("Instagram Random Comments", "Instagram Random Comments"),
        ("Instagram Likes [Post Link]", "Instagram Likes [Post Link]"),
        ("Instagram Followers", "Instagram Followers"),
    )
    service = models.CharField(max_length=200, choices=SERVICE_NAME, default=SERVICE_NAME[0])
    price = models.FloatField(default=0)

    def __str__(self):
        return self.service


class TikTokService(models.Model):
    SERVICE_NAME = (
        ("Tiktok Like [Post Link]", "Tiktok Like [Post Link]"),
        ("TikTok Followers", "TikTok Followers"),
        ("Cheapest TikTok Video Views [Post Link]", "Cheapest TikTok Video Views [Post Link]s")
    )

    service = models.CharField(max_length=200, choices=SERVICE_NAME, default=SERVICE_NAME[0])
    price = models.FloatField(default=0)

    def __str__(self):
        return self.service