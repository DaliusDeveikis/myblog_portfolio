from django.contrib import admin

from .models import UserBlog

class UserBlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(UserBlog, UserBlogAdmin)