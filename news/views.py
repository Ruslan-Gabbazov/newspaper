from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import View

from .forms import TagForm, NewsForm
from .models import News, Tag
from .utils import ObjectContentMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin


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


class NewsCreate(ObjectCreateMixin, View):
    form_model = NewsForm
    template = 'news/news_create_form.html'


class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = 'news/tag_create_form.html'


class NewsUpdate(ObjectUpdateMixin, View):
    model = News
    form_model = NewsForm
    template = 'news/news_update_form.html'


class TagUpdate(View):
    model = Tag
    form_model = TagForm
    template = 'news/tag_update_form.html'


class NewsDelete(ObjectDeleteMixin, View):
    model = News
    template = 'news/news_delete_form.html'
    redirect_url = 'news_list_url'


class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    template = 'news/tag_delete_form.html'
    redirect_url = 'tags_list_url'
