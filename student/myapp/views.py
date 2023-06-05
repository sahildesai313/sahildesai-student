from django.shortcuts import render,redirect
from .models import Register

# Create your views here.
def updateprofile(request):
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
    return render(request,"updateprofile.html")
