from datetime import datetime
from distutils.command.upload import upload
from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    STATUS_CHOICES = (
        ("d","draft"),
        ("p","published"),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100 , unique=True)
    body = models.TextField()
    image = models.ImageField(upload_to="images")
    publish = models.DateTimeField(auto_now_add=True)
    create = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    status = models.CharField(max_length=1 , choices=STATUS_CHOICES)

    def __str__(self):
        return self.title

    