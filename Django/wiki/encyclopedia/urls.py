from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/", views.index, name="wiki_index"),
    path("wiki/<str:title>", views.wiki_view, name="wiki_page"),
    path("create_new_page/", views.wiki_add, name="wiki_add"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("random", views.wiki_random, name="wiki_random")
]
