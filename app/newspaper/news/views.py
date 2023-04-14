from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


# Create your views here.

def news_list(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>Hello world</h1>')
