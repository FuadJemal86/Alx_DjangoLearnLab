# accounts/urls.py
from django.urls import path , include
from .views import PostViewSet, CommentViewSet , FeedView ,like_post , unlike_post
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/' , FeedView.as_view() , name='feed'),
    path("<int:pk>/like/", like_post.as_view(), name="like_post"),
    path("<int:pk>/unlike/", unlike_post.as_view(), name="unlike_post"),
]
