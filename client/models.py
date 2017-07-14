from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

class Client(AbstractUser):
    phone_number = PhoneNumberField()
    title = models.CharField(max_length=200, null=True, blank=True)
    balance = models.FloatField(default=0)
