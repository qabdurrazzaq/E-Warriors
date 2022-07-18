from django.db import models
from django.conf import settings
# Create your models here.

class SellWaste(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , null=True , blank=True , unique=False)
    title = models.CharField(max_length=50,null=True,blank=True,default=None)
    description = models.TextField(max_length=150,null=True,blank=True)
    pickup_address = models.TextField(max_length=150,null=True,blank=True)
    drop_address = models.TextField(max_length=150,null=True,blank=True)
    price = models.DecimalField(decimal_places = 2, max_digits = 100,null=True,blank=True)
    active = models.BooleanField(default=True)
    is_admins = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)

    def get_price(self):
        return self.price
