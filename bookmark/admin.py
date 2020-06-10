from django.contrib import admin
from bookmark.models import Bookmark, Marklist

# Register your models here.
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Marklist)
class MarklistAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')