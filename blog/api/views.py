<<<<<<< HEAD
=======
from rest_framework.generics import RetrieveAPIView, ListAPIView
from .serializers import PostSerializer
from blog.models import Post


class PostListAPIView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            "request": self.request
        })
        return context


class PostRetrieveAPIView(RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'
>>>>>>> main
