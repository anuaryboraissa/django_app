from django.db import models

# Create your models here.
class UserAccount(models.Model):
    email=models.EmailField(null=False,blank=False)
    password:models.TextField(null=False,blank=False)
