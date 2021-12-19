from django.urls import path
from .views import (
    RegisterView,
    AccountUpdateView,
    AccountDetailView,
    CommentListView,
    CommentUpdateView,
    CommentDeleteView
)

app_name = 'account'
urlpatterns = [
    path('signup/', RegisterView.as_view(), name='register'),
    path('', AccountDetailView.as_view(), name='home'),
    path('update/', AccountUpdateView.as_view(), name='update'),
    path('comments/', CommentListView.as_view(), name='comments'),
    path('comments/update/<pk>', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/delete/<pk>', CommentDeleteView.as_view(), name='comment-delete'),
]
