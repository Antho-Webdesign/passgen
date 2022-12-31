from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from accounts.models import User, Profile


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

    return render(request, 'users/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')


def profile(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'users/profile.html', context)

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
    return render(request, 'users/updt-profile.html')

def register(request):
    if request.method == "POST":
        # traiter le formulaire
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        if password == password2:
            user = User.objects.create_user(username, email, password)
            profile = Profile.objects.create(user=user)
            user.save()
            profile.save()
            login(request, user)
            return redirect('home')
        else:
            message = "Passwords do not match"
            msg = {
                'message': message
            }
            return render(request, 'users/register.html', msg)
    return render(request, 'users/register.html')

def reset_password(request):
    return render(request, 'users/password_reset.html')

def reset_password_done(request):
    return render(request, 'users/password_reset_done.html')

def reset_password_confirm(request):
    return render(request, 'users/password_reset_confirm.html')

def reset_password_complete(request):
    return render(request, 'users/password_reset_complete.html')



