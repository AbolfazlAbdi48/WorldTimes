from rest_framework import serializers
from news.models import Comment, Category, Tag, News


class CommentHyperlinkedSerializer(serializers.ModelSerializer):
    def get_owner(self, obj):
        return {
            "id": obj.owner.id,
            "username": obj.owner.username,
        }

    def get_created_time(self, obj):
        return {
            "created_time": obj.get_created_time(),
            "created_date": obj.get_created_date(),
        }

    owner = serializers.SerializerMethodField('get_owner')
    created = serializers.SerializerMethodField('get_created_time')

    class Meta:
        model = Comment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
