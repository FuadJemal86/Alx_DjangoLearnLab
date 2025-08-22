# accounts/urls.py
from django.urls import path , include
from .views import PostViewSet, CommentViewSet , FeedView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'feed', FeedView)

urlpatterns = [
    path('', include(router.urls)),
]
