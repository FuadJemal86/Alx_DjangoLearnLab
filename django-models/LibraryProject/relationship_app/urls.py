# relationship_app/urls.py
from django.urls import path
from .views import list_books
from .views import LibraryDetailView , register
from django.contrib.auth.views import LoginView , LogoutView
from . import views


urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    
    # ✅ register view from views module
    path('register/', views.register, name='register'),
]
