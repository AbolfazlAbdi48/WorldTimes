from django.urls import path
from .views import (
    home,
    NewsByCategoryListView,
    NewsByTagListView
)

app_name = 'news'
urlpatterns = [
    path('', home, name="home"),
    path('category/<slug>/', NewsByCategoryListView.as_view(), name="news-by-category"),
    path('tag/<slug>/', NewsByTagListView.as_view(), name="news-by-tag"),
]
