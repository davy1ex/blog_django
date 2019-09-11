from django.contrib import admin
from myblog.models import Article

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Article)