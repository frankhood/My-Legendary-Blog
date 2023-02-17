from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "id",
            "author",
            "title",
            "slug",
            "text",
            "created_date",
            "published_date",
            "image",
            "url"
        )

    def get_image(self, obj):
        if obj and obj.image:
            return obj.image.url
        return ""

    def get_url(self, obj):
        if obj and obj.id:
            request = self.context.get("request")
            return request.build_absolute_uri(obj.get_absolute_url())
        return ""