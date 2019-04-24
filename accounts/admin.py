from django.contrib import admin
from accounts.models import Profile
from memo.models import Memo

# Register your models here.
admin.site.register(Profile)
admin.site.register(Memo)