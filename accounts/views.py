from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm
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
        form = CustomUserCreationForm(request.POST)
        if form.is_valid() :
            user = form.save()
            # 사용자가 새로 생생될때마다 Profile을 생성하고 nickname을 아이디로 자동설정한다.
            Profile.objects.create(user=user,nickname=user.username)
            return redirect('accounts:login')

    form = CustomUserCreationForm()
    content = {
        'form' :form,
    }
    return render(request,'accounts/signup.html',content)
