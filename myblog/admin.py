from django.contrib import admin
from myblog.models import Article, Comment

class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Article)
admin.site.register(Comment)