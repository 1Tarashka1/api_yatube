from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from api.views import GroupViewSet, PostViewSet, CommentViewSet


router = DefaultRouter()

router.register(
    prefix='groups',
    viewset=GroupViewSet,
)
router.register(
    prefix='posts',
    viewset=PostViewSet,
)
router.register(
    prefix=r'posts/(?P<post_id>\d+)/comments',
    viewset=CommentViewSet,
    basename='comments',
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
