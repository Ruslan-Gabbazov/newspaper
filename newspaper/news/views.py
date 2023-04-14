from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


# Create your views here.

def news_list(request: HttpRequest):
    variables = [42 for _ in range(10)]
    return render(request, 'news/index.html', context={'variables': variables})
