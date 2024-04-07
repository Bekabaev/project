from django.urls import path
from .models import Post
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]