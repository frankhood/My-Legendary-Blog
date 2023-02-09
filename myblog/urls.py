from django.urls import path, include
from django.contrib import admin
from django.conf.urls import static
from django.conf import settings
from blog import urls as blog_urls

urlpatterns = [
    path('', include(blog_urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("api/v1/", include("blog.api.urls")),
]

urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
