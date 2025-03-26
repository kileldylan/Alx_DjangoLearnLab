from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer, CommentSerializer, FeedPostSerializer
from .models import Post, Comment
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view, permission_classes

# Post viewset to handle post-related logic
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author']
    search_fields = ['title', 'content'] 
    ordering_filters = ['created_at', 'updated_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=False, methods=['get'], 
            permission_classes=[IsAuthenticated])
    def feed(self, request):
   
        following_users = request.user.following.all()
        queryset = Post.objects.filter(author__in=following_users).order_by('-created_at')

        # Paginate results
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = FeedPostSerializer(
                page, 
                many=True,
                context={'request': request}
            )
            return self.get_paginated_response(serializer.data)
        
        serializer = FeedPostSerializer(
            queryset, 
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

# Comment viewset to handle comment-related logic
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # Returning comments only for the specified post
    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_pk'])

    # Setting logged-in user as the author
    def perform_create(self, serializer):
        post_id = self.request.data.get('post')
        serializer.save(author=self.request.user, post_id=post_id)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def feed_posts(request):
    followed_users = request.user.following.values_list('followed_id', flat=True)
    posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
    # Serialize posts (adjust based on your serializer)
    return Response({"posts": posts})