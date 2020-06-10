from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark, Marklist

from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin

# Create your views here.
class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark
    
class MarklistLV(ListView):
    model = Marklist

class MarklistDV(DetailView):
    model = Marklist

class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['name']
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class BookmarkChangeLV(LoginRequiredMixin, ListView):
    template_name = 'bookmark/bookmark_change_list.html'

    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)
        
class BookmarkUpdateView(OwnerOnlyMixin, UpdateView):
    model = Bookmark
    fields = ['name']
    success_url = reverse_lazy('bookmark:index')

class BookmarkDeleteView(OwnerOnlyMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')
    
class MarkCreateView(LoginRequiredMixin, CreateView):
    model = Marklist
    fields = ['book', 'title', 'url']
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class MarkChangeLV(LoginRequiredMixin, ListView):
    template_name = 'bookmark/marklist_change_list.html'

    def get_queryset(self):
        return Marklist.objects.filter(owner=self.request.user)
        
class MarkUpdateView(OwnerOnlyMixin, UpdateView):
    model = Marklist
    fields = ['book', 'title', 'url']
    success_url = reverse_lazy('bookmark:marklist_index')

class MarkDeleteView(OwnerOnlyMixin, DeleteView):
    model = Marklist
    success_url = reverse_lazy('bookmark:marklist_index')
    