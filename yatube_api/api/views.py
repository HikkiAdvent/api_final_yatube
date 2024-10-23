from django.shortcuts import get_object_or_404
from rest_framework import filters, validators, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.permissions import AuthorPermission
from api.serializers import (CommentSerializer, FollowSerializer,
                             GroupSerializer, PostSerializer)

from posts.models import Follow, Group, Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorPermission, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorPermission, IsAuthenticatedOrReadOnly)

    def get_post(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post

    def get_queryset(self):
        post = self.get_post()
        return post.comments.all()

    def perform_create(self, serializer):
        post = self.get_post()
        serializer.save(author=self.request.user, post=post)

    def perform_update(self, serializer):
        comment = self.get_object()
        serializer.save(author=comment.author, post=comment.post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('following__username', 'user__username')

    def get_queryset(self):
        user = self.request.user
        return Follow.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        following = serializer.validated_data['following']
        if user == following:
            raise validators.ValidationError(
                'Нельзя подписаться на самого себя.'
            )
        serializer.save(user=user)
