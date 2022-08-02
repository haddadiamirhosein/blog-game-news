from datetime import datetime
from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    STATUS_CHOICES = (
        ("d","draft"),
        ("p","published"),
    )
    title = models.CharField(max_length=200 , verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=100 , unique=True , verbose_name='آدرس مقاله')
    body = models.TextField( verbose_name='متن مقاله')
    image = models.ImageField(upload_to="images" , verbose_name='عکس مقاله')
    publish = models.DateTimeField(auto_now_add=timezone.now , verbose_name='تاریخ انتشار')
    create = models.DateTimeField(auto_now_add=True , verbose_name='زمان تولید')
    update = models.DateTimeField(auto_now=True , verbose_name='تارخ بروزرسانی')
    status = models.CharField(max_length=1 , choices=STATUS_CHOICES , verbose_name='وضعیت')

    def __str__(self):
        return self.title
    
    def show_less(self):
        return self.body[:71] + " ..."
    
    class Meta():
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    