from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model) :
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True)