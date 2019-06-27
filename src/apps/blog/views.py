from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, CreateView, View
from .forms import PostCreateForm
from .models import Post


User = get_user_model()


class AuthorList(ListView):
    model = User
    template_name = 'blog/author_list.html'
    context_object_name = 'authors'

    def get_queryset(self):
        current_user = self.request.user
        qs = super().get_queryset()
        if current_user.is_authenticated:
            subscribed_pk_list = [
                user.pk for user in current_user.subscriptions.all()
            ]
            qs = qs.exclude(pk=current_user.pk)
            qs = qs.exclude(pk__in=subscribed_pk_list)
        return qs


class SubscriptionsList(LoginRequiredMixin, ListView):
    template_name = 'blog/subscriptions_list.html'
    context_object_name = 'subscriptions'

    def get_queryset(self):
        current_user = self.request.user
        return current_user.subscriptions.all()


class SubscribeView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        current_user = request.user
        if current_user.pk == pk:
            return HttpResponseRedirect(reverse('blog:author-list'))
        try:
            subscribing_user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            messages.error(request, _('subscribing error'))
            return HttpResponseRedirect(reverse('blog:author-list'))
        current_user.subscriptions.add(subscribing_user)
        messages.success(request, _('successfuly subscribed'))
        return HttpResponseRedirect(reverse('blog:author-list'))


class UnsubscribeView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        current_user = request.user
        try:
            unsubscribing_user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            messages.error(request, _('unsubscribing error'))
            return HttpResponseRedirect(reverse('blog:subscriptions'))
        current_user.subscriptions.remove(unsubscribing_user)
        messages.success(request, _('successfuly unsubscribed'))
        return HttpResponseRedirect(reverse('blog:subscriptions'))


class PostCreate(LoginRequiredMixin, CreateView):
    template_name = 'blog/create_post.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('blog:subscriptions')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        return super().form_valid(form)
