from django.conf import settings
from django.db import models
from django.urls import NoReverseMatch, reverse_lazy, reverse
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.CharField("Slug", max_length=255)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField("Image")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        try:
            return reverse_lazy("post-detail", kwargs={'id': self.id})
        except NoReverseMatch:
            ...
        return ""
        
