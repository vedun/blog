# -*- coding: utf-8 -*-
from django.urls import path
from .views import AuthorList, SubscribeView, UnsubscribeView, \
    SubscriptionsList, PostCreate, MyPostsList, NewsFeed, MarkAsRead, \
    PostDetail

app_name = 'blog'

urlpatterns = [
    path('', AuthorList.as_view(), name='author-list'),
    path('subscribe/<int:pk>/', SubscribeView.as_view(), name='subscribe'),
    path(
        'unsubscribe/<int:pk>/', UnsubscribeView.as_view(), name='unsubscribe'
    ),
    path('subscriptions/', SubscriptionsList.as_view(), name='subscriptions'),
    path('post/add/', PostCreate.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('my_posts/', MyPostsList.as_view(), name='my-posts-list'),
    path('news_feed/', NewsFeed.as_view(), name='news-feed'),
    path('mark_as_read/<int:pk>/', MarkAsRead.as_view(), name='mark-as-read'),
]
