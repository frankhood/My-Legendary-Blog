from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "created_date", "published_date",)
    list_filter = ("author", "title", "published_date")
    search_fields = ("title", "slug",)
    prepopulated_fields = {"slug": ["title"]}
    fieldsets = (
        (
            "Post attributes",
            {
                "fields": (
                    ("author",),
                    ("title",),
                    ("slug",),
                    ("text",),
                    ("image",),
                    ("created_date", "published_date",),
                )
            },
        ),
    )