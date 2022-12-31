<<<<<<< HEAD
from PIL import Image
from django.contrib.auth.models import User, AbstractUser
from django.db import models

class User(AbstractUser):
    pass

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_img/', blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
=======
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Customer(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(Customer, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='prod/profile_img/',default='prod/profile_img/default.png', null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
>>>>>>> github/main

    def __str__(self):
        return self.user.username

<<<<<<< HEAD
    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.image.path)
=======
    class Meta:
        verbose_name_plural = 'Profiles'
        ordering = ('user',)



>>>>>>> github/main
