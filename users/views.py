from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from clubs.models import Club
#email config
from django.core.mail import send_mail
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

def send_email_with_html(request,receiverEmail,userId):
    subject = 'Django Email with HTML Content'
    from_email = 'anuaryissa21@gmail.com'
    recipient_list = [receiverEmail]
    # Load the HTML template
    context = {    
        'id': userId,
    }
    email_html = render(request, 'html/email_content.html', context).content.decode('utf-8')
    send_mail(
        subject,
        'Text content of the email (if needed)',
        from_email,
        [receiverEmail],
        html_message=email_html,
    )


# Create your views here.
@api_view(["GET","POST"])
def home_view(request):
    try:
        if request.method=="GET":
            users=User.objects.all()
            mapped_users=(UserSerializer(user).data for user in users)  
            return Response({"message":"successfully fetched","response":mapped_users})
        elif request.method=="POST":   
            userSerializer=UserSerializer(data=request.data)
            if userSerializer.is_valid():
                new_user=userSerializer.save()
                serialized_data=userSerializer.data
                send_email_with_html(request=request,receiverEmail=request.data['email'],userId=serialized_data['id'])
                return Response({"message":"user successfully saved","response":serialized_data})
            else:
                return Response(userSerializer.errors)
             
        else:
         return Response({"message":"default message returned","response":None})
    except Exception as e:
        print("Exception occurred =====================>")
        return Response({"message":str(e),"response":None})
     
@api_view(["GET","DELETE","PUT"])
def home_edu(request,pk):
    filter_user=User.objects.filter(id=pk)
    if filter_user.exists():   
        user=User.objects.get(id=pk)
        if request.method=="DELETE":
        
            if user is not None:
                user.delete()
                return Response({"message":"user deleted"})
            
            return Response({"message":"user doesn't exists"})
        elif request.method=="PUT":
            if user is not None:
                data=request.data
                user.first_name= data['first_name'] or user.first_name
                user.last_name= data['last_name'] or user.last_name
                user.phone_number= data['phone_number'] or user.phone_number
                user.gender= data['gender'] or user.gender
                user.user_type= data['user_type'] or user.user_type
                user.username= data['username'] or user.username
                user.email= data['email'] or user.email
                user.photo=data['photo'] if 'photo' in data  else user.photo
                if "club" in data:
                      print("assign club ===========> ")
                      filtered_club=Club.objects.filter(id=data['club'])
                      if filtered_club.exists():
                            print("assign club second ===========> ") 
                            club=filtered_club.first()
                            user.club=club
                      else:
                         print(" second Else ===========> ")
                else:
                    print(" Actual Else ===========> ")
                serialized_data=UserSerializer(user).data
                serialize=UserSerializer(data=serialized_data)
                if serialize.is_valid():
                    print("valid ======================> ")
                    user.save()
                    return Response({"message":"user updated"})
                return Response({"message":"user data is not valid"})
            
            return Response({"message":"user doesn't exists"})
        elif request.method=="GET":
            if user is not None:
                serialized_user=UserSerializer(user).data
                return Response({"message":"user fetched","user":serialized_user})
            
            return Response({"message":"user doesn't exists"})
    
        else:
            return Response({"message":f"Nothing to return {pk}"})
    else:
         return Response({"message":"user completely doesn't exists"})
     

class ExampleAPIView(APIView):
   
    def get(self,request,pk=None):
        if pk is None:
            return Response({"message":"just request get"})
        return Response({"message":f"request get {pk}"})
    def post(self,request):
        return Response({"message":"request post"})
    def delete(self,request,pk):
        return Response({"message":f"request delete {pk}"})
    def put(self,request,pk):
        return Response({"message":f"request update {pk}"})


