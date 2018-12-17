from rest_framework import serializers
from posts.models import Post, User, Like, Follow


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True,
                                                view_name='post-detail',
                                                read_only=True)
    follows = serializers.SlugRelatedField(slug_field='username',
                                           read_only=True,
                                           many=True)
    
    user_link = serializers.HyperlinkedIdentityField(view_name='user-detail', format='html')

    class Meta:
        model = User
        fields = ('id', 'username', 'follows', 'posts', 'user_link')
        lookup_field = 'username'


class FollowSerializer(serializers.ModelSerializer):
    followed_user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    follow_link = serializers.HyperlinkedIdentityField(view_name='follow-detail',
                                                       format='html')

    class Meta:
        model = Follow
        fields = ('followed_user', 'follow_link')



class PostSerializer(serializers.ModelSerializer):
    # poster = serializers.ReadOnlyField(source='poster.username')
    post_link = serializers.HyperlinkedIdentityField(view_name='post-detail',
                                                     format='html')
    poster = UserSerializer(read_only=True)



    class Meta:
        model = Post
        fields = ('text', 'poster', 'post_link')

    def create(self, validated_data):
        """
        Make new post with validated data.
        """
        return Post.objects.create(**validated_data)


class LikeSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    like_link = serializers.HyperlinkedIdentityField(view_name='like-detail',
                                                     format='html')

    class Meta:
        model = Like
        fields = ['user', 'post', 'like_link']