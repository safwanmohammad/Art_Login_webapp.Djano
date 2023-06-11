from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from . models import Register
     
# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        USERNAME = request.POST.get('username', '')
        PASSWORD = request.POST.get('password','')
        C_PASSWORD = request.POST.get('password1','')
        EMAIL = request.POST.get('email','')
        PHONE_NO = request.POST.get('Phone_no','')

        if PASSWORD == C_PASSWORD:
            if User.objects.filter(username=USERNAME).exists():
                messages.info(request, 'Oops UserName already taken')
                print("Oops UserName already taken")
                return redirect('sign_up')
            elif User.objects.filter(email=EMAIL).exists():
                messages.info(request, 'Oops email already taken')
                return redirect('sign_up')

            else:
                USER = User(
                    username=USERNAME,
                    password=make_password(PASSWORD),
                    email=EMAIL,
                )
                USER.save()
                messages.success(request, f'Hello  {USERNAME} \n'
                                          f'Your Account has been created successfully')
                print("user created...")
                return redirect('login')
        else:
            messages.warning(request,'Hy its,Password is not matching')
            print("password not matching")
            return redirect('sign_up')
    return render(request, 'sign_up.html')
