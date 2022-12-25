from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from accounts.models import User


# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == "" or password == "":
            return redirect('login')
        user = User.objects.get(username=username)
        login(request, user)
        return redirect('profile')

    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')


def profile(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'accounts/profile.html', context)

def edit_profile(request):
    user = request.user
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')

        if username == "" or email == "":
            return redirect('profile')
        else:
            user.username = username
            user.email = email
            user.save()
            return redirect('profile')
    return render(request, 'accounts/updt-profile.html')

def register(request):
    user = request.user
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if username == "" or email == "" or password == "":
            return redirect('register')
        user = User.objects.create_user(username=username, email=email, password=password, password2=password2)
        user.save()
        login(request, user)
        return redirect('profile')
    context = {
        'user': user,
    }
    return render(request, 'accounts/register.html', context)

def reset_password(request):
    return render(request, 'accounts/password_reset.html')

def reset_password_done(request):
    return render(request, 'accounts/password_reset_done.html')

def reset_password_confirm(request):
    return render(request, 'accounts/password_reset_confirm.html')

def reset_password_complete(request):
    return render(request, 'accounts/password_reset_complete.html')



