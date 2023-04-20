from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import View

from .models import News, Tag


# Create your views here.

def news_list(request: HttpRequest) -> HttpResponse:
    news = News.objects.all()
    return render(request, 'news/index.html', context={'news': news})


def tags_list(request: HttpRequest) -> HttpResponse:
    tags = Tag.objects.all()
    return render(request, 'news/tags_list.html', context={'tags': tags})


class NewsContent(View):

    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        news = get_object_or_404(News, slug__iexact=slug)
        return render(request, 'news/news_content.html', context={'news': news})


class TagContent(View):

    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        tag = get_object_or_404(Tag, slug__iexact=slug)
        return render(request, 'news/tag_content.html', context={'tag': tag})
