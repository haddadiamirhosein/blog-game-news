from django.contrib import admin
from . import models

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','slug','publish','status','create')
    list_filter = ('publish','status')
    search_fields = ('title','body')
    prepopulated_fields = {'slug':('title',)}
    ordering = ["publish","status"]
admin.site.register(models.Article , ArticleAdmin)