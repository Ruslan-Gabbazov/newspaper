from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .models import News


# Create your views here.

def news_list(request: HttpRequest) -> HttpResponse:
    news = News.objects.all()
    return render(request, 'news/index.html', context={'news': news})


def news_content(request: HttpRequest, slug: str) -> HttpResponse:
    news = News.objects.get(slug__iexact=slug)
    return render(request, 'news/news_content.html', context={'news': news})

