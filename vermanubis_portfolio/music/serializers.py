from rest_framework import serializers
from music.models import Music

# Music Serializer
class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'