from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Register
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

# Create your views here.
def profile(request):
    if request.method == "POST":
        username=request.POST.get('username')
        firstname= request.POST.get('firstname')
        lastname= request.POST.get('lastname')
        phone=request.POST.get('phone')
        try:
            mymember = Register.objects.get(username=username)
            newfname=firstname
            newlname=lastname
            newphone=phone
            mymember.firstname=newfname
            mymember.lastname=newlname
            mymember.phone=newphone
            mymember.save()
            return redirect('/home')
        except Register.DoesNotExist:
            print(mymember)
        return redirect('/login')
    return render(request,"profile.html")


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = Register.objects.get(username=username,password=password)
        if user is not None:
          
            messages.success(request, 'Successfully Logged In')
            return redirect('/home')

        else:
            return HttpResponse("hiii")
            
            messages.error(request, 'Invalid USER ID') 
    return render(request,'login.html')


@login_required(login_url='/')
def logout(request):
    return redirect('login')


def forgot(request):
    if request.method == "POST":
        username = request.POST.get('username')
        code = 1234
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirm_Password')

        if password == confirmpassword:
            user = Register.objects.get(username=username)
            new_password = password
            user.password=new_password
            new_confirmpassword=confirmpassword
            user.confirmpassword=new_confirmpassword
            
            user.save()
            return redirect('login')
        else:
            return redirect('/forgot')
    return render(request, 'forgot.html')


# def register(request):
#      if request.method=="POST":
#         username=request.POST.get('username')
#         firstname=request.POST.get('firstname')
#         lastname=request.POST.get('lastname')
#         phone=request.POST.get('phone')
#         email=request.POST.get('email')
#         password=request.POST.get('password')
#         confirmpassword=request.POST.get('confirmpassword')
#         if Register.objects.filter(username=username).exists():
#             return HttpResponse("user name is already extsts")

#         if len(phone) != 10:
#             return HttpResponse("number not a valid")
#         if password!=confirmpassword:
#             return HttpResponse("password did't match")
#         else:

            
#             register = Register(username=username,firstname=firstname,lastname=lastname,phone=phone,email=email,password=password,confirmpassword=confirmpassword)
#             register.save()
            
       
#             return redirect ('/')
#      return render(request,'register.html')  
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

def home(request):
    # user= Register.objects.all().values()
    # print(user)
    return render(request,'home.html')