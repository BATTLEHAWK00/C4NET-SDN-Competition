from django.db import models


# Create your models here.
class Admin(models.Model):
    username = models.CharField(max_length=32)
    passwd = models.CharField(max_length=128)
    salt = models.CharField(max_length=8)
    reg_time = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True)
