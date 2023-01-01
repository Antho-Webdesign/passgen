from django.db import models
from django.utils import timezone

<<<<<<< HEAD
from accounts.models import Customer
=======
from users.models import Customer
>>>>>>> parent of d84b1191 (app ok)


# Create your models here.
class GenPass(models.Model):
    user = models.OneToOneField(Customer, on_delete=models.CASCADE)
    site = models.CharField(max_length=30)
    time = models.DateTimeField(default=timezone.now)
    passwords = models.CharField(max_length=300)

    def __str__(self):
        return self.site

    class Meta:
        verbose_name = 'genpass'
        verbose_name_plural = 'genpasses'
        ordering = ['user']



