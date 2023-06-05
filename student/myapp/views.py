from django.shortcuts import render,redirect
from .models import Register
from django.http import HttpResponse


# Create your views here.

def register(request):
     if request.method=="POST":
        username=request.POST.get('username')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        if Register.objects.filter(username=username).exists():
            return HttpResponse("user name is already extsts")

        if len(phone) != 10:
            return HttpResponse("number not a valid")
        if password!=confirmpassword:
            return HttpResponse("password did't match")
        else:

            
            register = Register(username=username,firstname=firstname,lastname=lastname,phone=phone,email=email,password=password,confirmpassword=confirmpassword)
            register.save()
            
       
            return redirect ('/')
     return render(request,'register.html')  
    