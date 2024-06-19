from rest_framework import permissions, viewsets

from archive.models import Resource
from .serializers import ResourceSerializer


class ResourceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows resources to be viewed or edited.
    """
    queryset = Resource.objects.all().order_by("anon_title")
    serializer_class = ResourceSerializer
    permission_classes = [permissions.IsAuthenticated]
