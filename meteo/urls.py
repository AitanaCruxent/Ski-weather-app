from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("skiresorts/", views.skiresorts, name="skiresorts"),
    path("summits/", views.summits, name="summits"),
    path("bpa/", views.bpa, name="bpa"),
]
    