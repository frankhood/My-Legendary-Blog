from django.urls import path, include
from django.contrib import admin
from django.conf.urls import static
from django.conf import settings
<<<<<<< HEAD
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
=======
from blog import urls as blog_urls
>>>>>>> main

urlpatterns = [
    path('', include(blog_urls)),
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    # path('', include('blog.urls')),
    # path('api-auth/', include('rest_framework.urls'))
]


# urlpatterns += [
#     path("api/v1/", include("blog.api.urls")),
# ]

# Decommentare per servire i files statici e i media
# urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    path('api-auth/', include('rest_framework.urls')),
    path("api/v1/", include("blog.api.urls")),
]

urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
>>>>>>> main
