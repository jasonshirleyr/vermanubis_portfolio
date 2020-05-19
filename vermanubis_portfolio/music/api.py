from music.models import Music
from rest_framework import viewsets, permissions
from .serializers import MusicSerializer

# Music Viewset 
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MusicSerializer