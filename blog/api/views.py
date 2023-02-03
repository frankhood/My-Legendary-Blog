from rest_framework.generics import RetrieveAPIView, GenericAPIView, ListAPIView
from .serializers import PostSerializer
from blog.models import Post


class PostListDetailAPIView(ListAPIView, RetrieveAPIView, GenericAPIView):
    
    serializer_class = PostSerializer
    lookup_url_kwarg = "slug"

    def get_queryset(self):
        return Post.objects.all()
    
    