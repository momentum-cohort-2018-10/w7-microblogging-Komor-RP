from django.db import models
from django.contrib.auth.models import AbstractUser
from posts.validation import min_post_length


class User(AbstractUser):
    users_followed = models.ManyToManyField(
        to='User',
        through='Follow',
        through_fields=('following_user', 'followed_user'),
        related_name='follows'
    )

    USERNAME_FIELD = 'username'


class Timestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Follow(Timestamp):
    following_user = models.ForeignKey(User,
                                       on_delete=models.CASCADE,
                                       related_name='follows_from')
    followed_user = models.ForeignKey(User,
                                      on_delete=models.CASCADE,
                                      related_name='follows_to')


class Post(Timestamp):
    text = models.TextField(max_length=280, validators=[min_post_length])
    poster = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               null=True,
                               related_name='posts')


class Like(Timestamp):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'post'),)
