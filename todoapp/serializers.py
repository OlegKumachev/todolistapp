from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import serializers

from todoapp.models import Tasks, Tag


class TasksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']