from rest_framework import serializers
from music.models import About

# Music Serializer
class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'