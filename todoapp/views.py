from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.viewsets import ModelViewSet

from .models import Tasks
from .serializers import TasksSerializers


# Create your views here.

class TaskViewSet(ModelViewSet):
    queryset = Tasks.objects.all().order_by('title')
    serializer_class = TasksSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['is_completed', 'tags', 'title']
    ordering_filter = ['due_date', 'created_date', 'title']

