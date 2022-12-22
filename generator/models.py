from django.db import models
from django.utils import timezone

from users.models import Customer


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



