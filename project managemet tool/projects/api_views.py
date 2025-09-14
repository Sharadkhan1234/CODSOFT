from rest_framework import viewsets, permissions
from .models import Project, Task, Comment
from .serializers import ProjectSerializer, TaskSerializer, CommentSerializer
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all(); serializer_class = ProjectSerializer; permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all(); serializer_class = TaskSerializer; permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all(); serializer_class = CommentSerializer; permission_classes = [permissions.IsAuthenticatedOrReadOnly]
