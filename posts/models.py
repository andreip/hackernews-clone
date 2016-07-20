from __future__ import unicode_literals

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
