from rest_framework import serializers
from posts.models import Post, User, Like


class UserSerializer(serializers.HyperlinkedModelSerializer):
    post_set = serializers.HyperlinkedRelatedField(many=True,
                                                   view_name='post-detail',
                                                   read_only=True)
    # follow = serializers.SerializerMethodField('get_follow_names')

    class Meta:
        model = User
        fields = ('id', 'username', 'follow', 'post_set')
        lookup_field = 'username'

    def get_follow_names(self, user):
        return [follow.username for follow in user.follow.all()]


class PostSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source='poster.username')
    post_link = serializers.HyperlinkedIdentityField(view_name='post-detail',
                                                     format='html')

    class Meta:
        model = Post
        fields = ('text', 'poster', 'post_link')

    def create(self, validated_data):
        """
        Make new post with validated data.
        """
        return Post.objects.create(**validated_data)


class LikeSerializer(serializers.HyperlinkedModelSerializer):
    like_link = serializers.HyperlinkedIdentityField(view_name='like-detail',
                                                     format='html')

    class Meta:
        model = Like
        fields = ['user', 'post', 'like_link']