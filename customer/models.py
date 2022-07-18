from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , null=True , blank=True)
    first_name = models.CharField(max_length=120,null=True,blank=True)
    middle_name = models.CharField(max_length=120,null=True,blank=True)
    last_name = models.CharField(max_length=120,null=True,blank=True)
    phone_number = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.user)