from django.db import models

# Create your models here.
class Club(models.Model):
    name=models.TextField(null=False,blank=False)
    region=models.TextField(null=False,blank=False)
    district=models.TextField(null=False,blank=False)
    ward=models.TextField(null=False,blank=False)
    street=models.TextField(null=False)
    reg_number=models.TextField(null=False,blank=False)
    icon=models.TextField()
    description=models.TextField(null=False)
    
