from music.models import About
from rest_framework import viewsets, permissions
from .serializers import AboutSerializer

# Music Viewset 
class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AboutSerializer