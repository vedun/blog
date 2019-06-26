# -*- coding: utf-8 -*-
from django.urls import path
from .views import AuthorList, SubscribeView

app_name = 'blog'

urlpatterns = [
    path('', AuthorList.as_view(), name='author-list'),
    path('subscribe/<int:pk>/', SubscribeView.as_view(), name='subscribe'),
]
