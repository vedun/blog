# -*- coding: utf-8 -*-
from django.urls import path
from .views import AuthorList

app_name = 'blog'

urlpatterns = [
    path('', AuthorList.as_view(), name='author-list'),
]
