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

@login_required
def update(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)
    if request.method == 'POST' :
        form = MemoForm(request.POST, instance=memo)
        if form.is_valid() :
            form.save()
            return redirect('memos:list')
    form = MemoForm(instance=memo)
    content = {
        'form' :form,
    }
    return render(request,'memos/update.html',content)

@login_required
def delete(request,memo_id) :
    memo = get_object_or_404(Memo,pk=memo_id)
    if request.method == 'POST' :
        memo.delete()
    return redirect('memos:list')

@login_required
def like(request,memo_id) :
    memo = get_object_or_404(Memo,pk=memo_id)
    if request.user in memo.like_users.all() :
        memo.like_users.remove(request.user)
    else :
        memo.like_users.add(request.user)
    return redirect('memos:list')

@login_required
def people(request,user_id) :
    # user = get_object_or_404(get_user_model(),pk=user_id)
    # content = {
    #     'user' : user,
    # }
    return render(request, 'memos/people.html')