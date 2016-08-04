from django.conf.urls import url

from posts.views import PostListView, PostDetailView

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='post-list'),
    url(r'(?P<pk>[\d+])$', PostDetailView.as_view(), name='post-detail'),
]
