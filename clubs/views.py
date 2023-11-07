from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ClubSerializer
from .models import Club

# Create your views here.
class ClubApiView(APIView):
   
    def get(self,request,pk=None):
        if pk is not None:
            filtered=Club.objects.filter(id=pk)
            if filtered.exists():
               print(f"hello {filtered.first()}")
               serializedClub=ClubSerializer(filtered.first())
               return Response({"message":"club fetched","data":serializedClub.data})
            return Response({"message":"Club doesn't exists","data":None})
        else:
            clubs=Club.objects.all()
            serialized_data=(ClubSerializer(club).data for club in clubs)
            return Response({"message":"Items fetched","clubs":serialized_data})
    def post(self,request):
        serializer=ClubSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save()  
             return Response({"message":"data valid","data":serializer.data})
        return Response({"message":"something is not ok!"})
    def put(self,request,pk):
        filtered=Club.objects.filter(id=pk)
        if filtered.exists():
           club=filtered.first()
           data=request.data
           club.name=data["name"] if "name" in data else club.name
           club.icon=data["icon"] if "icon" in data else club.icon
           club.region=data["region"] if "region" in data else club.region
           club.district=data["district"] if "district" in data else club.district
           club.ward=data["ward"] if "ward" in data else club.ward
           club.street=data["street"] if "street" in data else club.street
           club.description=data["description"] if "description" in data else club.description
           club.reg_number=data["reg_number"] if "reg_number" in data else club.reg_number
           club.save()
           return Response({"message":"club updated successfully!","data":ClubSerializer(club).data})
        return Response({"message":"CLub doesn't exists"})
       
    def delete(self,request,pk):
            filtered=Club.objects.filter(id=pk)
            if filtered.exists():
               club=filtered.first()
               club.delete()
               return Response({"message":"club deleted"})
            return Response({"message":"Club doesn't exists"})