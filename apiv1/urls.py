from django.urls import path, include
from apiv1 import views as api_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', api_views.UserViewSet)
router.register('likes', api_views.LikeViewSet)

urlpatterns = [
    path('', api_views.api_root),
    path('', include(router.urls)),
    path('posts/', api_views.PostList.as_view(), name='post-list'),
    path('posts/<pk>', api_views.PostDetail.as_view(), name='post-detail'),
]
