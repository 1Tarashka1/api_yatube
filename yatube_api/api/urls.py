from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register(
    'posts',
    PostViewSet,
    basename='Post'
)
router.register(
    'groups',
    GroupViewSet,
    basename='Group'
)
router.register(
    'follow',
    FollowViewSet,
    basename='Follow'
)
router.register(
    r'posts/(?P<id>[0-9]+)/comments',
    CommentViewSet,
    basename='Comment'
)

urlpatterns = [
    path(
        'v1/api-token-auth/',
        views.obtain_auth_token,
        name='obtain_auth_token'
    ),
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
