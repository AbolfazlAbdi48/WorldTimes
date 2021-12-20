from rest_framework import serializers
from news.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


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
