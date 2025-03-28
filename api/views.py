from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed

import api.serializers as sl
from api.permissions import IsAuthorOrReadOnly
from posts.models import Group, Post
from .serializers import GroupSerializer

API_PERMISSIONS = [IsAuthenticated, IsAuthorOrReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    """ViewSet для модели Group."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed('PUT method is not allowed.')

    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed('PATCH method is not allowed.')
    
    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed('POST method is not allowed for creating groups.')


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet для модели Post."""

    permission_classes = API_PERMISSIONS
    queryset = Post.objects.all()
    serializer_class = sl.PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet для модели Comment."""

    permission_classes = API_PERMISSIONS
    serializer_class = sl.CommentSerializer

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())
