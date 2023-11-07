from rest_framework import serializers
from .models import Event,EventAttachment,EventGallery
from django import forms

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields="__all__"

class AttachmentSerializer(forms.ModelForm):
    class Meta:
        model=EventAttachment
        fields="__all__"

class EventGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model=EventGallery
        fields="__all__"
        
    def validate(self,data):
        file_name=data.get("file_name")
        file_size=data.get("file_size")
        file_data=data.get("file_data")
       
        if not file_name.endswith((".jpg",".png",".jpeg")):
            raise serializers.ValidationError("Invalid file")
        if  file_size > (5*1024*1024):
            raise serializers.ValidationError("File size exceeds 5 MB") 
        return data




