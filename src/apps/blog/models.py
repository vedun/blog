from django.urls import reverse
from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from .utils import new_post_email


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, models.CASCADE,
        verbose_name=_('Post author'),
    )
    title = models.CharField(verbose_name=_('Title'), max_length=4096)
    body = models.TextField(
        verbose_name=_('Body'),
        validators=[validators.MinLengthValidator(5)],
    )
    creation_date = models.DateTimeField(
        verbose_name=_('Creation date'), auto_now_add=True,
    )

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ('pk',)

    def __str__(self):
        return f'{self.author}:{self.title}'


class PostReader(models.Model):
    post = models.ForeignKey(
        Post, models.CASCADE,
        verbose_name=_('Post'),
    )
    reader = models.ForeignKey(
        settings.AUTH_USER_MODEL, models.CASCADE,
        verbose_name=_('Reader'),
    )

    class Meta:
        verbose_name = _('Post reader')
        verbose_name_plural = _('Posts readers')
        ordering = ('pk',)
        unique_together = ('post', 'reader')


def send_emails(sender, **kwargs):
    if kwargs['created']:
        new_post = kwargs['instance']
        new_post_email(
            new_post.author.subscribers.all(),
            #  FIXME: лучше пока ничего не придумал
            'http://localhost:8000{}'.format(
                reverse('blog:post-detail', kwargs={'pk': new_post.pk})
            ),
        )
post_save.connect(send_emails, sender=Post)
