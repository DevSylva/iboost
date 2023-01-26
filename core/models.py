from django.db import models
from account.models import User
from django.utils import timezone
from uuid import uuid4
import datetime

# Create your models here.
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user)


class DepositPreview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.FloatField(default=0)
    method = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.amount)


class DepositLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    gateway = models.CharField(max_length=30, null=True, blank=True)
    amount = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=30, null=True, blank=True)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.gateway


class InstagramService(models.Model):

    SERVICE_NAME = (
        ("Real Nigerian Instagram Follower", "Real Nigerian Instagram Follower"),
        ("Instagram Reach + Impressions + Profile Visits [Post Link]", "Instagram Reach + Impressions + Profile Visits [Post Link]"),
        ("Instagram Reach + Impressions [Post Link]", "Instagram Reach + Impressions [Post Link]"),
        ("Instagram Emoji Comments", "Instagram Emoji Comments"),
        ("Instagram Random Comments", "Instagram Random Comments"),
        ("Instagram Views [Post Link]", "Instagram Views [Post Link]"),
        ("Instagram Likes [Post Link]", "Instagram Likes [Post Link]"),
        ("Instagram Followers", "Instagram Followers"),
    )
    service = models.CharField(max_length=150, choices=SERVICE_NAME, default="choose", null=True, blank=True, unique=True)
    minimum = models.PositiveIntegerField()
    maximum = models.PositiveIntegerField()
    price_per_k = models.FloatField(default=0)
    service_id = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.service


class TiktokService(models.Model):

    SERVICE_NAME = (
        ("Tiktok Like [Post Link]", "Tiktok Like [Post Link]"),
        ("TikTok Followers", "TikTok Followers"),
        ("Cheapest TikTok Video Views [Post Link]", "Cheapest TikTok Video Views [Post Link]s"),
    )
    service = models.CharField(max_length=150, choices=SERVICE_NAME, default="choose", null=True, blank=True, unique=True)
    minimum = models.PositiveIntegerField()
    maximum = models.PositiveIntegerField()
    price_per_k = models.FloatField(default=0)
    service_id = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.service


class YoutubeService(models.Model):

    SERVICE_NAME = (
        ("Youtube Views [RECOMMENDED]", "Youtube Views [RECOMMENDED]"),
        ("Youtube Subscribers", "Youtube Subscribers"),
        ("Youtube Likes", "Youtube Likes"),
    )
    service = models.CharField(max_length=150, choices=SERVICE_NAME, default="choose", null=True, blank=True, unique=True)
    minimum = models.PositiveIntegerField()
    maximum = models.PositiveIntegerField()
    price_per_k = models.FloatField(default=0)
    service_id = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.service


class OrderHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.CharField(max_length=150, null=True, blank=True)
    link = models.CharField(max_length=550, null=True, blank=True)
    quantity = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "Order History"
        verbose_name_plural = "Order Histories"

def create_id():
    now = datetime.datetime.now()
    return str(now.year)+str(now.month)+str(now.day)+str(uuid4())[:7]

class CourierService(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    tracking_id = models.CharField(primary_key=True, default=create_id, editable=False, max_length=30)
    # sender information
    sender_full_name = models.CharField(max_length=150)
    sender_package = models.CharField(max_length=500)
    sender_address = models.CharField(max_length=300)
    sender_country = models.CharField(max_length=150)
    sender_city = models.CharField(max_length=150)
    sender_state_province = models.CharField(max_length=150)
    sender_postal_code = models.CharField(max_length=150)
    sender_phone_number = models.CharField(max_length=150)
    sender_email = models.CharField(max_length=150)
    sender_type = models.CharField(max_length=150)

    # sender information
    receiver_full_name = models.CharField(max_length=150)
    receiver_shipping_fee = models.CharField(max_length=150)
    receiver_address = models.CharField(max_length=300)
    receiver_country = models.CharField(max_length=150)
    receiver_city = models.CharField(max_length=150)
    receiver_state_province = models.CharField(max_length=150)
    receiver_postal_code = models.CharField(max_length=150)
    receiver_phone_number = models.CharField(max_length=150)
    receiver_email = models.CharField(max_length=150)

    
    def __str__(self):
        return str(self.tracking_id)



class ContactSupport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    subject = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField()
    message = models.TextField(default="")

    def __str__(self):
        return str(self.user)