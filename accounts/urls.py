from django.urls import path

from accounts.views import login_user, logout_user, edit_profile, reset_password, reset_password_done, \
    reset_password_confirm, reset_password_complete, register, profile

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),  # Connexion

    # path('profile/', profile, name='profile'),  # Profil
    path('modifier-profile/', edit_profile, name="updt_profile"),
    # path('register/', register, name='register'),  # Inscription
    path('reset-password/', reset_password, name='reset_password'),
    path('reset-password-done/', reset_password_done, name='reset_password_done'),
    path('reset-password-confirm/<uidb64>/<token>/', reset_password_confirm, name='reset_password_confirm'),
    path('reset-password-complete/', reset_password_complete, name='reset_password_complete'),
]