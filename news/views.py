from django.shortcuts import render, get_object_or_404
from .models import News
from django.utils import timezone

def news(request):
    news = News.objects.order_by('-date')
    return render(request, 'news/includes/news_list.html', {'news': news})

def news_detail(request, pk):
    new = get_object_or_404(News, pk=pk)
    return render(request, 'news/includes/news_detail.html', {'new': new})

def add_comment(request, pk):
    new = get_object_or_404(News, pk=pk)
    return render(request, 'news/includes/news_detail.html', {'new': new})
    
    
