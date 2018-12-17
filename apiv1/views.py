from posts.models import Post, User, Like, Follow
from apiv1.serializers import PostSerializer, UserSerializer, LikeSerializer, FollowSerializer
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework.views import APIView
from rest_framework import permissions
from apiv1.permissions import IsOwnerOrReadOnly
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework import viewsets


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'posts': reverse('post-list', request=request, format=format),
        'likes': reverse('like-list', request=request, format=format),
        'follows': reverse('follow-list', request=request, format=format),
        'follow-posts': reverse('following-posts',
                                request=request,
                                format=format)
    })


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    lookup_field = 'pk'


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class FollowList(generics.ListCreateAPIView):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.follows_from

    def perform_create(self, serializer):
        serializer.save(following_user=self.request.user)


class FollowDetail(generics.RetrieveDestroyAPIView):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.follows_from


class FollowingPostList(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Post.objects.filter(
            poster__in=self.request.user.users_followed.all())


class PostList(generics.ListCreateAPIView):
    """
    CBV for posts
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)


class PostDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve, update, or delete a post
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)
