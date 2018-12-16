from django.contrib import admin
from posts.models import User, Post, Like, Follow


class FollowersInline(admin.StackedInline):
    model = Follow
    fk_name = 'following_user'
    fields = ('followed_user',)
    extra = 1


class UserAdmin(admin.ModelAdmin):
    model = User
    inlines = [FollowersInline]


class FollowAdmin(admin.ModelAdmin):
    model = Follow
    list_display = ('following_user', 'followed_user',)


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('text', 'poster',)


class LikeAdmin(admin.ModelAdmin):
    model = Like
    list_display = ('user', 'post',)


admin.site.register(User, UserAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)
