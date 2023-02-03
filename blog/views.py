from django.views.generic import TemplateView, DetailView
from . import models
# Create your views here.

class PostListTemplateView(TemplateView):
    template_name = "blog/post_list.html"

class PostDetailView(DetailView):
    template_name = "blog/post_detail.html"

    model = models.Post

