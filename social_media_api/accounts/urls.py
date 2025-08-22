# accounts/urls.py
from django.urls import path , include
from .views import RegisterView, LoginView, UserDetailView
from .views import PostViewSet, CommentViewSet , FollowerUserViewSet , UnFollowUserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('me/', UserDetailView.as_view(), name='user-detail'),
    path('', include(router.urls)),
    path('follow/int:user_id/', FollowerUserViewSet.as_view(), name='follow-user'),
    path('unfollow/int:user_id/', UnFollowUserViewSet.as_view(), name='unfollow-user'),
    
]
