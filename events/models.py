from django.db import models

# Create your models here.

class Event(models.Model):
    name=models.TextField(blank=False,null=False)
    description=models.TextField(blank=False,null=False)
    startDate=models.DateField(auto_now=True,null=False,blank=False)
    endDate=models.DateField(auto_now=True,null=False,blank=False)
    startTime=models.DateTimeField(blank=False,null=False,auto_now=True)
    endTime=models.DateTimeField(auto_now=True,null=False,blank=False)
    venue=models.CharField(max_length=200,null=False,blank=False)
    attachment=models.TextField(blank=True,null=False)
    
    
class EventAttachment(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    file=models.FileField(upload_to="uploads/",null=False,blank=False)
class EventGallery(models.Model):
    file_name=models.TextField(blank=False,null=False)
    file_size=models.PositiveBigIntegerField(null=False,blank=False)
    file_data=models.TextField(null=False,blank=False)
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
