from rest_framework import serializers
from .models import UserAccount

import re
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserAccount
        fields="__all__"
        
    def validate_password(self,password):
        strong_password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        if len(str(password))<6 or not  re.match(strong_password_pattern, password):
            raise serializers.ValidationError("Password is not strong")
        return password