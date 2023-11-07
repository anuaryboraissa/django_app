from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EventSerializer,AttachmentSerializer,EventGallerySerializer
import uuid
import os
from rest_framework import status
from django.conf import settings
from .models import EventAttachment,Event,EventGallery
import base64
from django.core.files.base import ContentFile



class EventApi(APIView):
    def get(self,request,pk=None):
        if pk  is not None:
            return Response({"message":f"Get request with id {pk}"})
        return Response({"message":"Get all request"})
    def post(self,request):
        serializer=EventSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response({"message":"Post data is valid request","data":serializer.data})
        return Response({"message":"Post request"})
    def put(self,request,pk):
        return Response({"message":f"Update request id {pk}"})
    def delete(self,request,pk):
        return Response({"message":f"Delete request id {pk}"})
    
class EventAttachmentApi(APIView):
    def get(self,request,pk=None):
        if pk  is not None:
            return Response({"message":f"Get request with id {pk}"})
        return Response({"message":"Get all request"})
    def post(self,request):
         serializer=AttachmentSerializer(request.POST,request.FILES)
         if serializer.is_valid():
           
            uploadFile(request)
            # serializer.save()
            return Response({"message":"Post Data is valid"})
         return Response({"message":serializer.errors})

    
    def put(self,request,pk):
        return Response({"message":f"Update request id {pk}"})
    def delete(self,request,pk):
        return Response({"message":f"Delete request id {pk}"})
        
        
        
class EventGalleryApi(APIView):
    def get(self,request,pk=None):
        if pk  is not None:
            return Response({"message":f"Get request with id {pk}"})
        return Response({"message":"Get all request"})
    def post(self,request):
         serializer=EventGallerySerializer(data=request.data)
         if serializer.is_valid():
             try:
              decoded_data = base64.b64decode(request.data['file_data'])
              file_to_upload=ContentFile(decoded_data)
              uploadGallery(self,file_to_upload,request.data['event'],request.data['file_size'],request.data['file_name'])
             except ValueError:
                return Response({'error': 'Invalid base64 data'}, status=status.HTTP_400_BAD_REQUEST)
             return Response({"message":"Post data serializer is valid"})
         return Response({"message":serializer.errors})
    def put(self,request,pk):
        return Response({"message":f"Update request id {pk}"})
    def delete(self,request,pk):
        return Response({"message":f"Delete request id {pk}"})
        
       

def uploadFile(self, request):
        uploaded_file=request.FILES['file']
        file_ext=os.path.splitext(uploaded_file.name)[-1]
        upload_dir=os.path.join(settings.MEDIA_ROOT,"uploads")
        os.makedirs(upload_dir,exist_ok=True)
        uuid_str=str(uuid.uuid4())
        new_file_name=f"{uuid_str}{file_ext}"
        new_file_path=os.path.join(upload_dir,new_file_name)
        with open(new_file_path, 'wb') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        event=Event.objects.get(id=request.data['event'])
        fileModel=EventAttachment(file=new_file_name,event=event)
        fileModel.save()
        
def uploadGallery(self, uploaded_file,eventID,fileSize,fileActualName):
        print(f"Step {uploaded_file}")
        file_ext=f".{str(fileActualName).split('.')[-1]}"
        upload_dir=os.path.join(settings.MEDIA_ROOT,"uploads")
        os.makedirs(upload_dir,exist_ok=True)
        uuid_str=str(uuid.uuid4())
        new_file_name=f"{uuid_str}{file_ext}"
        new_file_path=os.path.join(upload_dir,new_file_name)
        with open(new_file_path, 'wb') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        print(f"Event id {eventID}")
        event=Event.objects.get(id=int(eventID))
        fileModel=EventGallery(file_name=fileActualName,file_data=new_file_name,file_size=fileSize,event=event)
        fileModel.save()