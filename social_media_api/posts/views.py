from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fieldd = ['author']
    search_fields = ['title, content']
    ordering_filters = ['created_at', 'updated_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    #Returning comments only for the specified post
    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_pk'])
    
    #setting logged in user as the author
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)