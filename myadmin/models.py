from django.db import models

# Create your models here.
class Myadmin(models.Model):
    title = models.CharField(max_length=100, unique=True, default="default_theme")
    theme = models.TextField(default="", blank=True, null=True)

    def __str__(self):
        return self.title