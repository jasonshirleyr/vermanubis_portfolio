from rest_framework import serializers
from music.models import About
from music.models import Music

# About Serializer - used for storing the about section of music
class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

# Music Serilaizer - used to store links for the music page
class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'