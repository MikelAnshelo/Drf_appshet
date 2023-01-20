from .models import productos

from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
	queryset = productos.objects.all()
	permission_classes = [permissions.AllowAny]
	serializer_class = ProjectSerializer