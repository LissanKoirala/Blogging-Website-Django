from django.urls import path
from .views import (
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    CategoryView,
    LikeView,
    AddCommentView,
    LatestPostView
)
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('latest_posts/', LatestPostView.as_view(), name='latest-post'),
    path('photo_gallery/', views.photo_gallery, name='photo-gallery'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    path('enquiries/', views.enquiries, name='enquiries'),
    path('latest_videos/', views.latest_videos, name='video'),
    path('video/', views.video, name='video_one'),
    path('video_two/', views.video_two, name='video_two'),
    path('video_three/', views.video_three, name='video_three'),
    path('video_four/', views.video_four, name='video_four'),
    path('post/<int:pk>/comment', AddCommentView.as_view(), name='add_comment'),
    path('search', views.search, name="search"),
]
