from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self) -> str:
        return "{}".format(self.title)