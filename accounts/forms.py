from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Profile

class CustomUserCreationForm(UserCreationForm) :
    class Meta(UserCreationForm.Meta) :
        model = get_user_model()

class CustomProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["nickname","description","image"]
