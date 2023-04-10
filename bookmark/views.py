from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from bookmark.models import Bookmark

# Create your views here.

class BookmarkListView(ListView):
    model = Bookmark

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_create'