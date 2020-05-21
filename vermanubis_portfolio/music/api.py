from music.models import About, Music
from rest_framework import viewsets, permissions
from .serializers import AboutSerializer, MusicSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

# About Viewset 
class AboutViewSet(viewsets.ModelViewSet):

    queryset = About.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AboutSerializer

# Music Viewset
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MusicSerializer