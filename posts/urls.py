from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    DraftPostListView
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('drafts/', DraftPostListView.as_view(), name='draft_post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('<int:pl>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('new/', PostCreateView.as_view(), name='post_view'),
]