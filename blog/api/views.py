from rest_framework.generics import RetrieveAPIView, ListAPIView
from .serializers import PostSerializer
from blog.models import Post


class PostListAPIView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostRetrieveAPIView(RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'
