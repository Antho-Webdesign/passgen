from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
from .models import Profile

admin.site.register(Profile)
=======
from django.contrib.auth.admin import UserAdmin
<<<<<<<< HEAD:accounts/admin.py
from django.contrib.auth.models import Group

from accounts.models import Customer, Profile
========
from users.models import Customer, Profile
>>>>>>>> github/main:users/admin.py


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'


class CustomerAdmin(UserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_select_related = ('profile',)

    def get_inline_instances(self, request, obj=None):
        return [inline(self.model, self.admin_site) for inline in self.inlines]


admin.site.register(Customer)
<<<<<<<< HEAD:accounts/admin.py
admin.site.register(Profile)
admin.site.unregister(Group)
========
admin.site.register(Profile)
>>>>>>>> github/main:users/admin.py
>>>>>>> github/main
