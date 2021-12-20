from django.urls import path
from .views import (
    CommentAPIView,
    NewsListView,
    NewsDetailView,
    TagListView,
    CategoryListView
)

app_name = 'api'
urlpatterns = [
    path('comments/', CommentAPIView.as_view(), name='comment'),
    path('news/', NewsListView.as_view(), name='comment'),
    path('news/<pk>', NewsDetailView.as_view(), name='comment'),
    path('categories/', TagListView.as_view(), name='comment'),
    path('tags/', CategoryListView.as_view(), name='comment'),
]
