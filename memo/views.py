from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Memo
from .forms import MemoForm

# Create your views here.
def index(request) :
    memos = Memo.objects.all()
    content = {
        'memos' : memos
    }
    return render(request,'memos/list.html', content)

@login_required
def create(request) :
    if request.method == 'POST' :
        form = MemoForm(request.POST)
        if form.is_valid() :
            memo = form.save(commit=False)
            memo.user = request.user
            memo.save()
            return redirect('memos:list')
    form = MemoForm()
    content = {
        'form' :form,
    }
    return render(request,'memos/create.html', content)