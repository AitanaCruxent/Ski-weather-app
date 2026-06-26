from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("skiresorts/", views.skiresorts, name="skiresorts"),
    path("summits/", views.summits, name="summits"),
    path("bpa/", views.bpa, name="bpa"),
]
    