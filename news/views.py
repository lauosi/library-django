from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from .forms import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def news(request):
    news = News.objects.order_by('-date')
    return render(request, 'news/includes/news_list.html', {'news': news})

def news_detail(request, pk):
    new = get_object_or_404(News, pk=pk)
    return render(request, 'news/includes/news_detail.html', {'new': new})

def add_comment_to_news(request, pk):
    new = get_object_or_404(News, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = new
            comment.save()
            return redirect('news_detail', pk=new.pk)
    else:
        form = CommentForm()
    return render(request, 'news/includes/add_comment_to_news.html', {'form': form})

@login_required
def news_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.published_date = timezone.now()
            news.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = PostForm()
    return render(request, 'news/includes/news_add.html', {'form': form})

@login_required
def news_edit(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=news)
        if form.is_valid():
            news = form.save(commit=False)
            news.published_date = timezone.now()
            news.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = PostForm(instance=news)
    return render(request, 'news/includes/news_add.html', {'form': form})
    
    
