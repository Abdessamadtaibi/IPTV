from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.db import models
from django.utils.text import slugify

class Plan(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration_days = models.IntegerField()
    description = models.TextField(max_length=2000,default='')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.name} - ${self.price}"


class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_subscription = models.CharField(max_length=100,default='')
    modepass_subscription = models.CharField(max_length=100,default='')
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('expired', 'Expired')], default='active')

    def __str__(self):
        return f"{self.user.username} - {self.plan.name} ({self.status})"


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    payment_method = models.CharField(max_length=20)
    transaction_id = models.CharField(max_length=100, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of ${self.amount} by {self.user.username}"


class KeywordsDescriptionHome(models.Model):
    title = models.CharField(max_length=100,default='')
    head_keyword = models.TextField(max_length=500,default='')
    head_description = models.TextField(max_length=500,default='')
    alt_images_base = models.TextField(max_length=200,default='')
    alt_channels = models.TextField(max_length=200,default='')
    alt_series = models.TextField(max_length=200,default='')