from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListTemplateView.as_view(), name='post_list'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
]




