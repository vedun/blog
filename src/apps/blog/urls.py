# -*- coding: utf-8 -*-
from django.urls import path
from .views import AuthorList, SubscribeView, UnsubscribeView, \
    SubscriptionsList

app_name = 'blog'

urlpatterns = [
    path('', AuthorList.as_view(), name='author-list'),
    path('subscribe/<int:pk>/', SubscribeView.as_view(), name='subscribe'),
    path(
        'unsubscribe/<int:pk>/', UnsubscribeView.as_view(), name='unsubscribe'
    ),
    path('subscriptions/', SubscriptionsList.as_view(), name='subscriptions'),
]
