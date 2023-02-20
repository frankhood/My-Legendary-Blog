<<<<<<< HEAD


urlpatterns = [

=======
from django.urls import path
from blog.api import views as api_views

urlpatterns = [
    path("posts/", api_views.PostListAPIView.as_view(), name="post-list-api"),
    path("post/<int:id>/", api_views.PostRetrieveAPIView.as_view(), name="post-retrieve-api"),
>>>>>>> main
]