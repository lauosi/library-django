from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from .forms import PostForm, PostComment
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def news(request):
    news = News.objects.order_by('-date')
    return render(request, 'news/includes/news_list.html', {'news': news})

def news_detail(request, pk):
    new = get_object_or_404(News, pk=pk)
    return render(request, 'news/includes/news_detail.html', {'new': new})

def add_comment(request, pk):
    new = get_object_or_404(News, pk=pk)
    return render(request, 'news/includes/news_detail.html', {'new': new})

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
    
