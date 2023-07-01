from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Subscriber(AbstractUser):
    class Meta:
        verbose_name = 'Subscriber'
    dvg_points = models.PositiveIntegerField(default=0)
    wallet_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    transaction_pin = models.CharField(max_length=4)
  
    location = models.CharField(max_length=50)
    
