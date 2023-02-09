from django.shortcuts import render
from . import models


def post_list_view(request):
    context = {
        "object_list": models.Post.objects.all()
    }
    return render(request, "blog/post_list.html", context)


def post_detail_view(request, id):
    context = {
        "object": models.Post.objects.get(id=id)
    }
    return render(request, "blog/post_detail.html", context)
