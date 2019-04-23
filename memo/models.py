from django.db import models
from django.conf import settings

# Create your models here.
class Memo(models.Model) :
    title = models.CharField(max_length=50)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) :
        return f'{self.id} | {self.title} | {self.user}'