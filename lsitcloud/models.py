from django.db import models

# Create your models here.
class Cache(models.Model):
    title = models.CharField(max_length=100, unique=True, default="default_name")
    theme = models.TextField(default="", blank=True, null=True)

    def __str__(self):
        return self.title