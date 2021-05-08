from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path ("add_listing", views.add_listing, name="add_listing"),
    path ("listing_page/<str:listing_title>", views.listing_page, name="listing_page"),
    path ("watch", views.watch, name="watch"),
    path ("unwatch", views.unwatch, name="unwatch"),
    path ("watchlist", views.watchlist, name="watchlist"),
    path ("make-a-bid", views.make_a_bid, name="make a bid"),
    path ("close", views.close, name="close auction"),
]
