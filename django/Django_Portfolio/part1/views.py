from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Liquor, Comment
from .forms import LiquorForm, CommentForm

# Create your views here.
@require_safe
def index(request):
    liquors = Liquor.objects.order_by('-pk')
    context = {
        'liquors': liquors,
    }
    return render(request, 'part1/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = LiquorForm(request.POST)
        if form.is_valid():
            liquor = form.save(commit=False)
            liquor.user = request.user
            liquor.save()
            return redirect('part1:detail', liquor.pk)
    else:
        form = LiquorForm()
    context = {
        'form': form,
    }
    return render(request, 'part1/create.html', context)


@require_safe
def detail(request, article_pk):
    liquor = get_object_or_404(Liquor, pk=article_pk)
    comment_form = CommentForm()
    # 조회한 Liquor의 모든 댓글을 조회(역참조)
    comments = liquor.comment_set.all()
    context = {
        'liquor': liquor,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'part1/detail.html', context)


@require_POST
def delete(request, pk):
    liquor = get_object_or_404(Liquor, pk=pk)
    print(liquor)
    if request.user.is_authenticated:
        if request.user == liquor.user:
            liquor.delete()
    return redirect('part1:index')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    Liquor = get_object_or_404(Liquor, pk=pk)
    if request.user == Liquor.user:
        if request.method == 'POST':
            form = LiquorForm(request.POST, instance=Liquor)
            if form.is_valid():
                Liquor = form.save()
                return redirect('part1:detail', Liquor.pk)
        else:
            form = LiquorForm(instance=Liquor)
    else:
        return redirect('part1:index')
    context = {
        'Liquor': Liquor,
        'form': form,
    }
    return render(request, 'part1/update.html', context)


@require_POST
def comment_create(request, pk):
    if request.user.is_authenticated:
        Liquor = get_object_or_404(Liquor, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.Liquor = Liquor
            comment.user = request.user
            comment.save()
        return redirect('part1:detail', Liquor.pk)
    return redirect('accounts:login')


@require_POST
def comment_delete(request, Liquor_pk ,comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('part1:detail', Liquor_pk)


@require_POST
def likes(request, Liquor_pk):
    if request.user.is_authenticated:
        Liquor = get_object_or_404(Liquor, pk=Liquor_pk)

        if Liquor.like_users.filter(pk=request.user.pk).exists():
            Liquor.like_users.remove(request.user)
        else:
            Liquor.like_users.add(request.user)
        
        return redirect('part1:index')
    return redirect('accounts:login')