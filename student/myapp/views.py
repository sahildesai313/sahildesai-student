from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Register
from django.contrib.auth.models import User
from django.contrib  import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    # user= Register.objects.all().values()
    # print(user)
    return render(request,'home.html')