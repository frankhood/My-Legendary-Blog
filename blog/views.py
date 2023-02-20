<<<<<<< HEAD
=======
from django.shortcuts import render
from . import models
from django.urls import reverse, reverse_lazy


def post_list_view(request):
    context = {
        "object_list": models.Post.objects.all(),
        "post_list_api_url": request.build_absolute_uri(reverse_lazy("post-list-api"))
    }
    return render(request, "blog/post_list.html", context)

def my_blog_templte(request):
    context = {
        "object_list": models.Post.objects.all()
    }
    return render(request, "blog/post_list.html", context)


def post_detail_view(request, id):
    context = {
        "object": models.Post.objects.get(id=id)
    }
    return render(request, "blog/post_detail.html", context)
>>>>>>> main
