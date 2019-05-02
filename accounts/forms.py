from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Profile
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm) :
    class Meta(UserCreationForm.Meta) :
        model = get_user_model()

class CustomProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["nickname"]
        widgets = {
            'nickname' : forms.TextInput(
                attrs = {
                    'placeholder' : '닉네임'
                }
            )
        }
        labels = {
            'nickname': _('닉네임'),
        }
        help_texts = {
            'nickname': _('닉네임을 입력해주세요.'),
        }

class CustomProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["nickname","description","image"]
        
