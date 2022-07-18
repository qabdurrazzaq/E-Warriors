from django.db import models
from django.conf import settings

# Create your models here.

class Dealer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , default = None)
    first_name = models.CharField(max_length=120,null=True,blank=True)
    middle_name = models.CharField(max_length=120,null=True,blank=True)
    last_name = models.CharField(max_length=120,null=True,blank=True)
    phone_number = models.IntegerField(null=True,blank=True)
    stripe_secret_api = models.CharField(max_length=500,null=True,blank=True)
    stripe_pub_api = models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return str(self.user.username)