from django.db import models
from django.contrib.auth.models import AbstractUser


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

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Profiles'
        ordering = ('user',)
        app_label = "accounts"




'''
MDP 
- user
- url_origin
- time
- password
'''

'''
class MdpGenere(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    url_origin = models.CharField(max_length=30)
    date_enr = models.DateTimeField(default=timezone.now)
    passwords_generate = models.CharField(max_length=300)

    def __str__(self):
        return self.url_origin
'''