from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserDetail, resturants_details,Grocery_details
from django.contrib import messages
from django.template import loader




def profile(request):
    if "username" not in request.session:
        return redirect("login")
    if request.method == "POST":

        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phone = request.POST.get('phone')

        try:
            mymember = UserDetail.objects.get(
                username=request.session["username"])

            newfname = firstname
            newlname = lastname
            newphone = phone
            mymember.firstname = newfname
            mymember.lastname = newlname
            mymember.phone = newphone
            mymember.save()

            return redirect('/home')
        except UserDetail.DoesNotExist:
            return redirect('/login')
    user_data = UserDetail.objects.get(username=request.session["username"])
    return render(request, "profile.html", context={"mymember": user_data})


def login(request):
    context = {}
    if "username" in request.session:
        print("test")
        return redirect("home")

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = UserDetail.objects.filter(username=username, password=password)
        if user.exists():
            messages.success(request, 'Successfully Logged In')
            request.session["username"] = username
            return redirect('home')
        else:
            context["error"] = "Invalid username or password"
    return render(request, 'login.html', context=context)


def logout(request):
    del request.session["username"]
    return redirect('login')


def forgot(request):
    if "username" in request.session:
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get('username')
        code = 1234
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirm_Password')

        if password == confirmpassword:
            user = UserDetail.objects.get(username=username)
            new_password = password
            user.password = new_password
            new_confirmpassword = confirmpassword
            user.confirmpassword = new_confirmpassword

            user.save()
            return redirect('login')
        else:
            return redirect('/forgot')
    return render(request, 'forgot.html')


def register(request):
    if "username" in request.session:
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        if UserDetail.objects.filter(username=username).exists():
            messages.error(request, " username already exists")
            return redirect('register')

        if len(phone) != 10:
            messages.error(request, " number is not a valid")
            return redirect('register')

        if password != confirmpassword:
            messages.error(request, "Passwords do not match.")
            return redirect('register')
        else:
            register = UserDetail(username=username, firstname=firstname, lastname=lastname,
                                  phone=phone, email=email, password=password, confirmpassword=confirmpassword)
            register.save()

            return redirect('/')
    return render(request, 'register.html')


def homepage(request):
    if "username" not in request.session:
        return redirect("login")
    data = resturants_details.objects.all()
    datas=Grocery_details.objects.all()
    return render(request, 'home.html',context={'data':data,'datas':datas})

def rest(request, image_id):

    item = resturants_details.objects.get(id=image_id)
    template = loader.get_template('rest_detail.html')
    context = {
        'item': item,
        'id': id,
    }
    return HttpResponse(template.render(context, request))


def grocery(request,image_id):
    value=Grocery_details.objects.get(id=image_id)
    template = loader.get_template('grocery_details.html')
    context = {
    'value':value,
 
}
    return HttpResponse(template.render(context,request))

