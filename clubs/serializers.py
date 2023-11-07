from rest_framework import serializers
from .models import Club

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model=Club
        exclude=['icon',"club"]