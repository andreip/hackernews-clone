from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.utils.functional import cached_property
from django.db import models

from utils.models import TimeStampedModel


class Post(TimeStampedModel):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    upvotes = models.IntegerField(default=0)
    url = models.URLField(blank=True)
    text = models.CharField(max_length=2048, blank=True)

    class Meta:
        ordering = ('-upvotes', '-created')

    @cached_property
    def post_url(self):
        if self.url:
            return self.url
        return reverse('posts:post-detail', args=(self.pk,))
