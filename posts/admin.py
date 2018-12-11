from django.contrib import admin
from posts.models import User, Post, Like


class UserAdmin(admin.ModelAdmin):
    model = User
    filter_horizontal = ('follow',)


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('text', 'poster',)


class LikeAdmin(admin.ModelAdmin):
    model = Like
    list_display = ('user', 'post',)


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)
