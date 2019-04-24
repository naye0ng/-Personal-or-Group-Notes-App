from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


# Create your views here.
def login(request) :
    if request.method == 'POST' :
        form = AuthenticationForm(request.POST)
        if form.is_valid() :
            # 로그인하여 원래 주소로 넘겨주기
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'posts:list')

    form = AuthenticationForm()
    content = {
        'form' :form,
    }
    return render(request,'accounts/login.html',content)

def logout(request) :
    pass