from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    follow = models.ManyToManyField("self")

    USERNAME_FIELD = 'username'


class Timestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(Timestamp):
    text = models.TextField(max_length=280)
    poster = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Like(Timestamp):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)