from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sign_in(request):
    return HttpResponse("hey Login")
def sign_up(request,pk):
    print(f"Primary key {pk}")
    return render(request,"html/account_create.html")