from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import mixins
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.generics import get_object_or_404

from posts.models import Post, Group

from .permissions import IsAuthorOrReadOnly
from .serializers import (
    PostSerializer,
    GroupSerializer,
    CommentSerializer,
    FollowSerializer,
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthorOrReadOnly,
    ]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthorOrReadOnly,
    ]

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, pk=post_id)
        queryset = post.comments.all()
        return queryset

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        user = self.request.user
        queryset = user.followings.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
