from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.utils.functional import cached_property
from django.db import models
from django.utils.translation import ugettext_lazy as _

import urlparse

from utils.models import TimeStampedModel


class Post(TimeStampedModel):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    upvotes = models.IntegerField(default=0)
    url = models.URLField(blank=True)
    text = models.CharField(max_length=2048, blank=True)

    class Meta:
        ordering = ('-upvotes', '-created')

    def __unicode__(self):
        domain = urlparse.urlparse(self.url).netloc
        return u'%s (%s)' % (self.title, domain)

    @cached_property
    def post_url(self):
        if self.url:
            return self.url
        return reverse('posts:post-detail', args=(self.pk,))


class Comment(TimeStampedModel):
    author = models.ForeignKey('auth.User')
    upvotes = models.IntegerField(default=0)
    text = models.TextField()

    # The comment can have a parent be either a post or a comment itself.
    parent_comment = models.ForeignKey('Comment', related_name='comments',
                                       null=True, blank=True)
    parent_post = models.ForeignKey(Post, related_name='comments',
                                    null=True, blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.author, self.created)

    def clean(self):
        if self.parent_post and self.parent_comment:
            raise ValidationError(_('Cannot have a parent be both a post and a comment'))
