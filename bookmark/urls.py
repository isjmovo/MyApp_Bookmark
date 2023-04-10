from django.urls import path

from bookmark.views import BookmarkListView, BookmarkCreateView

urlpatterns = [
    path("", BookmarkListView.as_view(), name='list'),
    path("add/", BookmarkCreateView.as_view(), name='add'),
]