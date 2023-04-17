from django.urls import path
from .views import *

urlpatterns = [
    path('', news_list, name='news_list_url'),
    path('news/<str:slug>/', news_content, name='news_content_url')
]
