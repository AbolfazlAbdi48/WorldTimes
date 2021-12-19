from django.urls import path
from .views import CommentAPIView

app_name = 'api'
urlpatterns = [
    path('comments/', CommentAPIView.as_view(), name='comment')
]
