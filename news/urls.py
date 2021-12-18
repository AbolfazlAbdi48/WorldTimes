from django.urls import path
from .views import (
    home,
    NewsByCategoryListView,
    NewsByTagListView,
    NewsDetailView
)

app_name = 'news'
urlpatterns = [
    path('', home, name="home"),
    path('category/<slug>/', NewsByCategoryListView.as_view(), name="news-by-category"),
    path('tag/<slug>/', NewsByTagListView.as_view(), name="news-by-tag"),
    path('news/<pk>/<slug>/', NewsDetailView.as_view(), name="news-detail"),
]
