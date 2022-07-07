from django.db import models
from django.conf import settings


# Create your models here.
class Liquor(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    alcohol = models.PositiveIntegerField()
    size = models.PositiveIntegerField()
    img_url = models.URLField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    liquor = models.ForeignKey(Liquor, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content