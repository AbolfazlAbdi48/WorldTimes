from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CommentSerializer, CommentHyperlinkedSerializer
from news.models import Comment


# Create your views here.
class CommentAPIView(APIView):
    """
    Api Endpoint to list comments,
    METHOD: GET, POST.
    """

    def get(self, request, format=None):
        news_id = request.GET.get('news_id')
        comments = Comment.objects.filter(news_id=news_id).order_by('-id')
        serializer = CommentHyperlinkedSerializer(comments, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            owner = request.user
            serializer.validated_data['owner'] = owner
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
