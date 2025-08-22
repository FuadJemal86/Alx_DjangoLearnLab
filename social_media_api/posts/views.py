# accounts/views.py
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import PageNumberPagination

from social_media_api.notifications.models import Notification
from .models import Like, Post, Comment
from .serializers import PostSerializer , CommentSerializer




class IsAuthorOrReadOnly(permissions.BasePermission):
    """Allow only authors to edit/delete their objects."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)    

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # get the list of users the current user follows
        following_users = self.request.user.following.all()
        # fetch posts from those users, ordered by most recent
        return Post.objects.filter(author__in=following_users).order_by("-created_at")
  
@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    # Check if already liked
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    
    if created:
        # Only create a notification if this is a new like
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked",
            target=post
        )
        return JsonResponse({"status": "liked", "likes_count": post.like_set.count()})
    else:
        return JsonResponse({"status": "already_liked", "likes_count": post.like_set.count()})


@login_required
def unlike_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    # Remove the like if it exists
    like = Like.objects.filter(user=request.user, post=post).first()
    if like:
        like.delete()
        return JsonResponse({"status": "unliked", "likes_count": post.like_set.count()})
    else:
        return JsonResponse({"status": "not_liked", "likes_count": post.like_set.count()})    