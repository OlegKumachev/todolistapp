from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import serializers

from todoapp.models import Tasks


class TasksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id', 'title', 'description']
