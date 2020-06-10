from django.urls import path
# from bookmark.views import BookmarkLV, BookmarkDV
from bookmark import views


app_name = 'bookmark'
urlpatterns = [
    path('', views.BookmarkLV.as_view(), name='index'),

    path('bookmark/<int:pk>/', views.BookmarkDV.as_view(), name='bookmark_detail'),

    # Example : /bookmark/add/
    path('bookmark/add/', views.BookmarkCreateView.as_view(), name="bookmark_add"),

    # Example : /bookmark/change/
    path('bookmark/change/', views.BookmarkChangeLV.as_view(), name="bookmark_change"),

    # Example : /bookmark/99/update/
    path('bookmark/<int:pk>/update/', views.BookmarkUpdateView.as_view(), name="bookmark_update"),

    # Example : /bookmark/99/delete/
    path('bookmark/<int:pk>/delete/', views.BookmarkDeleteView.as_view(), name="bookmark_delete"),

    path('marklist/', views.MarklistLV.as_view(), name='marklist_index'),

    path('marklist/<int:pk>/', views.MarklistDV.as_view(), name='marklist_detail'),

    # Example : /marklist/add/
    path('marklist/add/', views.MarkCreateView.as_view(), name="marklist_add"),

    # Example : /marklist/change/
    path('marklist/change/', views.MarkChangeLV.as_view(), name="marklist_change"),

    # Example : /marklist/99/update/
    path('marklist/<int:pk>/update/', views.MarkUpdateView.as_view(), name="marklist_update"),

    # Example : /marklist/99/delete/
    path('marklist/<int:pk>/delete/', views.MarkDeleteView.as_view(), name="marklist_delete"),
]