from django.urls import path
from .views import *

urlpatterns = [
    path('', news_list, name='news_list_url'),
    path('news/<str:slug>/', NewsContent.as_view(), name='news_content_url'),
    path('tags/', tags_list, name='tags_as_view()list_url'),
    path('tags/create', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>', TagContent.as_view(), name='tag_content_url'),
]
