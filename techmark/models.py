from django.db import models

# Create your models here.
class techmark(models.Model):
    key = models.CharField(max_length=100, unique=True, default="techmark")
    value = models.TextField(default="", blank=True, null=True)

    def __str__(self):
        return self.key