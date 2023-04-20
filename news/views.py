from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import View

from .forms import TagForm
from .models import News, Tag
from .utils import ObjectContentMixin


# Create your views here.

def news_list(request: HttpRequest) -> HttpResponse:
    news = News.objects.all()
    return render(request, 'news/index.html', context={'news': news})


def tags_list(request: HttpRequest) -> HttpResponse:
    tags = Tag.objects.all()
    return render(request, 'news/tags_list.html', context={'tags': tags})


class NewsContent(ObjectContentMixin, View):
    model = News
    template = 'news/news_content.html'


class TagContent(ObjectContentMixin, View):
    model = Tag
    template = 'news/tag_content.html'


class TagCreate(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        form = TagForm()
        return render(request, 'news/tag_create.html', context={'form': form})
