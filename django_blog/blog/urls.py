from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='blog-home'),
    path('', views.IndexView.as_view(), name='blog-index'),
    path('post/<int:post_id>/', views.PostView.as_view(), name='blog-post'),
    path('post/<username>/', views.UserPostsHomeView.as_view(), name='user-posts'),
]
