from django.urls import path
<<<<<<< HEAD

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
=======
from .views import signup, login_user, logout_user, password_reset_form, password_reset_form_done, \
    password_reset_confirm, password_reset_complete, profile, edit_profile

urlpatterns = [
    # Inscription
    path('signup/', signup, name='signup'),
    # Connexion
    path('login/', login_user, name='login'),
    # Déconnexion
    path('logout/', logout_user, name='logout'),
    # profile
    path('profile/', profile, name='profile'),
    # edit profile
    path('edit_profile/', edit_profile, name='edit_profile'),
    # Reset password form
    path('password_reset/form/', password_reset_form, name='password_reset_form'),
    # Reset password done
    path('password_reset/done/', password_reset_form_done, name='password_reset_form_done'),
    # Reset password confirm
    path('password_reset/confirm/', password_reset_confirm, name='password_reset_confirm'),
    # Reset password complete
    path('password_reset/complete/', password_reset_complete, name='password_reset_complete'),
]
>>>>>>> github/main
