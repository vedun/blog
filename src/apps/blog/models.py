from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core import validators


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
