from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Register
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

# Create your views here.

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