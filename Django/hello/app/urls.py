from django.urls import path
from . import views

urlpatterns = [
  path ("", views.index, name="index"),
  path ('pragat', views.pragat, name="pragat"),
  path ('brian', views.brian, name="brian"),
  path ('david', views.david, name = "david")
]