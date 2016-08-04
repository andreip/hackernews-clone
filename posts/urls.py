from django.conf.urls import url

from posts.views import PostListView

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='post-list'),
    url(r'(?P<pk>[\d+])$', PostListView.as_view(), name='post-detail'),
]
