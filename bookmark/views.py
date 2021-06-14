from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Bookmark


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'


class BookmarkDetailView(DetailView):
    model = Bookmark


class BookmarkCreateView(CreateView):
    model = Bookmark  # 어떤 모델의 입력을 받을 것인지 결정
    fields = ['site_name', 'url']  # 어떤 필드들을 입력받을 것인지 설정
    success_url = reverse_lazy('list')  # 글쓰기를 완료하고 이동할 페이지 설정
    template_name_suffix = '_create'  # 사용할 템플릿의 접미사만 변경하는 설정값


class BookmarkListView(ListView):
    model = Bookmark
