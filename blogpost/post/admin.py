from django.contrib import admin

from . import models

class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'slugname', 'author', 'date')

admin.site.register(models.PostModel, AdminPost)