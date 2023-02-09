from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "author",
            "title",
            "slug",
            "text",
            "created_date",
            "published_date",
            "image",
        )

    def get_image(self, obj):
        if obj and obj.image:
            return obj.image.url
        return ""
