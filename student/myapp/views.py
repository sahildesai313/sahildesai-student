from django.shortcuts import render
from django.http import HttpResponse
from .models import Register
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def home(request):
    user= Register.objects.all().values()
    print(user)
    # return render (request,'home.html')
    return render(request,'home.html')