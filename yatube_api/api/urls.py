from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'groups', GroupViewSet, basename='group')
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    re_path(
        r'^v1/posts/(?P<post_id>\d+)/comments/$',
        CommentViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='post-comments-list',
    ),
    re_path(
        r'^v1/posts/(?P<post_id>\d+)/comments/(?P<pk>\d+)/$',
        CommentViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy',
        }),
        name='post-comments-detail',
    ),
    path(
        'v1/jwt/create/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair',
    ),
    path('v1/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(
        'v1/jwt/verify/',
        TokenVerifyView.as_view(),
        name='token_verify',
    ),
]
