from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Register
from django.contrib import messages


# Create your views here.
def profile(request):
    if "username" not in request.session:
        return redirect("login")
    if request.method == "POST":
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        try:
            mymember = Register.objects.get(
                username=request.session["username"])
            newfname = firstname
            newlname = lastname
            newphone = phone
            mymember.firstname = newfname
            mymember.lastname = newlname
            mymember.phone = newphone
            mymember.save()
            return redirect('/home')
        except Register.DoesNotExist:
            print(mymember)
        return redirect('/login')
    user_data = Register.objects.get(username=request.session["username"])
    return render(request, "profile.html", context={"mymember": user_data})


def login(request):
    context = {}
    if "username" in request.session:
        print("test")
        return redirect("home")

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = Register.objects.filter(username=username, password=password)
        if user.exists():

            messages.success(request, 'Successfully Logged In')
            print("login")
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
            user = Register.objects.get(username=username)
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
        if Register.objects.filter(username=username).exists():
            messages.error(request, " username already exists")
            return redirect('register')

        if len(phone) != 10:
            messages.error(request, " number is not a valid")
            return redirect('register')

        if password != confirmpassword:
            messages.error(request, "Passwords do not match.")
            return redirect('register')
        else:
            register = Register(username=username, firstname=firstname, lastname=lastname,
                                phone=phone, email=email, password=password, confirmpassword=confirmpassword)
            register.save()

            return redirect('/')
    return render(request, 'register.html')


def homepage(request):
    # user= Register.objects.all().values()
    # print(user)

    if "username" not in request.session:
        return redirect("login")

    print("user")
    print(request.session["username"])

    user_data = Register.objects.get(username=request.session["username"])

    return render(request, 'home.html', context={"user": user_data})
