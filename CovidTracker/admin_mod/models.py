from django.db import models
from ..UserModule.models import User


# Create your models here.
class Admin(models.Model):
    name = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=10)
    pinCode = models.CharField(max_length=6)


class CovidResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    status = [
        'positive', 'positive',
        'negative', 'negative'
    ]
    result = models.CharField(choices=status)

