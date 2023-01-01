from django.contrib.auth import get_user_model, logout, login, authenticate
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404

<<<<<<< HEAD
from .models import Profile

User = get_user_model()
=======
from accounts.models import User
>>>>>>> parent of d84b1191 (app ok)


# Create your views here.
def signup(request):

<<<<<<< HEAD
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
            return render(request, 'accounts/signup.html', msg)
    return render(request, 'accounts/signup.html')

def login_user(request):
    if request.method == "POST":
        # traiter le formulaire
        username = request.POST.get("username")
        password = request.POST.get("password")

        if user := authenticate(request, username=username, password=password):
            login(request, user)
            return redirect('home')
    return render(request, 'accounts/login.html')
=======
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
>>>>>>> parent of d84b1191 (app ok)


def logout_user(request):
    logout(request)
    return redirect('home')


def profile(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    context = {
        'profile': profile,
    }
    return render(request, 'accounts/profile.html', context)


def edit_profile(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    context = {
        'profile': profile,
    }
    if request.method == "POST":
        # traiter le formulaire
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        city = request.POST.get("city")
        zip_code = request.POST.get("zip_code")
        state = request.POST.get("state")
        country = request.POST.get("country")
        user.username = username
        user.email = email
        profile.phone = phone
        profile.address = address
        profile.city = city
        profile.zip_code = zip_code
        profile.state = state
        profile.country = country
        message = "Your profile has been updated successfully"
        msg = {
            'message': message,
        }
        context.update(msg)

        profile.save()
        return redirect('profile')
    return render(request, 'accounts/profile_update.html', context)


def password_reset_form(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if email := User.objects.get(email=email):
            # protocol = 'https'
            host = '127.0.0.1:8000/'
            link = 'accounts/password_reset/confirm/'
            send_mail('Password Reset', f'{host}{link}', ' ', [email], fail_silently=False)
            print(send_mail)
            return redirect('password_reset_form_done')

    return render(request, 'accounts/registration/password_reset_form.html')

def password_reset_form_done(request):
    return render(request, 'accounts/registration/password_reset_done.html')

def password_reset_confirm(request):
    return render(request, 'accounts/registration/password_reset_confirm.html')

def password_reset_complete(request):
    return render(request, 'accounts/registration/password_reset_complete.html')

