from django.urls import path

from . import views

app_name = "blogs"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:blog_id>/", views.detail, name="detail"),
    path("<int:blog_id>/update/", views.blog_update, name="blog_update"),
]