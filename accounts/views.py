from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomProfileCreationForm
from .models import Profile

# Create your views here.
def login(request) :
    if request.method == 'POST' :
        form = AuthenticationForm(request, request.POST)

        if form.is_valid() :
            # 로그인하여 원래 주소로 넘겨주기
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'memos:list')

    form = AuthenticationForm()
    content = {
        'form' :form,
    }
    return render(request,'accounts/login.html',content)

def logout(request) :
    auth_logout(request)
    return redirect('memos:list')


def signup(request) :
    if request.method =='POST' :
        user_form = CustomUserCreationForm(request.POST)
        profile_form = CustomProfileCreationForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid() :
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            # Profile.objects.create(user=user,nickname=user.username)
            return redirect('accounts:login')

    user_form = CustomUserCreationForm()
    profile_form = CustomProfileCreationForm()
    content = {
        'user_form' : user_form,
        'profile_form' : profile_form,
    }
    return render(request,'accounts/signup.html',content)
