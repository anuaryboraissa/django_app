from rest_framework import serializers
from .models import User
from clubs.models import Club

class CustomClubSerializer(serializers.ModelSerializer):
    class Meta:
        model=Club
        fields=["name","id",'region',"district","description"]


class UserSerializer(serializers.ModelSerializer):
    # club=CustomClubSerializer()
    club = serializers.PrimaryKeyRelatedField(queryset=Club.objects.all(), allow_null=True, required=False)
    # name=serializers.CharField(source="club.name",read_only=True)
    # icon=serializers.CharField(source="club.icon",read_only=True)
    class Meta:
        model=User
        fields="__all__"
        depth=1
        # depth=1
    def validate(self,data):
       
        first_name=data.get("first_name")
        last_name=data.get("last_name")
        phone_number=str(data.get("phone_number"))
        gender=str(data.get("gender"))
        user_type=str(data.get("user_type"))
        username=str(data.get("username"))
        email=str(data.get("email"))
        genders=["MALE","FEMALE"]
        user_types=["NORMAL_USER","MENTOR","REGULATOR"]
      
        if len(str(first_name)) < 3:
            raise serializers.ValidationError("First Name must have at least 2 characters")
        elif len(str(last_name)) < 3:
            raise serializers.ValidationError("Last Name must have at least 2 characters")
        elif not (phone_number.startswith("+2557") or phone_number.startswith("+2556")) or str((not phone_number[4:len(phone_number)])).isdigit() or len(str(phone_number))!=13: 
             raise serializers.ValidationError("Phone number is not valid")
        elif gender not in genders:
             raise serializers.ValidationError("Gender number is not valid")
        elif user_type not in user_types:
             raise serializers.ValidationError("User type not valid")
        elif len(username) < 4:
             raise serializers.ValidationError("Username is not valid")
        elif User.objects.filter(email=email).exists():
             raise serializers.ValidationError("User with that email already exists")
        elif User.objects.filter(username=username).exists():
            raise serializers.ValidationError("User with that Username already exists")
        return data