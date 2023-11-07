from django.db import models
from clubs.models import Club

# Create your models here.
class User(models.Model):
    first_name=models.TextField(null=False,blank=False)
    last_name=models.TextField(null=False,blank=False)
    email=models.EmailField(null=False,blank=False)
    username=models.TextField(null=False,blank=False)
    photo=models.TextField(blank=True)
    phone_number=models.TextField(null=False,blank=False)
    gender=models.CharField( max_length=10)
    user_type=models.TextField(null=False,blank=False)
    club=models.ForeignKey(Club,on_delete=models.CASCADE,null=True,)