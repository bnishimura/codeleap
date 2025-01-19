
from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'title', 'created_datetime', 'content', 'username')
        # fields = '__all__'

    title = serializers.CharField(required=True)
    content = serializers.TextField(required=True)
    username = serializers.CharField(required=True)

    id = serializers.IntegerField(read_only=True)
    created_datetime = serializers.DateTimeField(read_only=True)

