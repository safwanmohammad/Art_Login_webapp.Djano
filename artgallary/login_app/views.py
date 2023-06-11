from django.contrib import messages, auth
from django.shortcuts import render, redirect

# Create your views here.
def login(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(req, user)
            return redirect('/')
        else:
            messages.info(req, 'invalid Username or Password')
            return redirect('login')
    return render(req,'login.html')


def logout(request):
    auth.logout(request)
    print("log out")
    return redirect('/')


# def login(request):
#     if request.method == 'POST':
#         USERNAME = request.POST.get('username')
#         PASSWORD = request.POST.get('password')
#         if Register.objects.filter(user_name=USERNAME).exists():
#             if Register.objects.filter(password=PASSWORD).exists():
#                 messages.info(request, f'welcome {USERNAME}')
#                 print(User)
#                 return redirect('/')
#             else:
#                 messages.info(request, 'invalid Password')
#             return redirect('login')
#         else:
#             messages.info(request, 'invalid UserName')
#             return redirect('login')

#     return render(request,'login.html')
