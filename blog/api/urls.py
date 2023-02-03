
from django.urls import path
from blog.api import views as api_views

urlpatterns = [
    path("post/", api_views.PostListDetailAPIView.as_view(), name="post-list-api"),
    path("post/<slug:slug>/", api_views.PostListDetailAPIView.as_view(), name="post-detail-api"),
]