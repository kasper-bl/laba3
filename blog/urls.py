from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import RegisterView

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/post_delete/', views.PostDeleteView.as_view(), name='post_delete'),
]
