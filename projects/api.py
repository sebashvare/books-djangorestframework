from .models import Projects
from rest_framework import viewsets, permissions
from .serializer import ProjectSerializers

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializers