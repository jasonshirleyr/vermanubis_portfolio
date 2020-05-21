from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import About, Music
from .serializers import AboutSerializer, MusicSerializer
from .api import AboutViewSet

@api_view(['GET','DELETE', 'UPDATE'])
def get_delete_update_about(request, pk):
    try:
        about = About.objects.get(pk = pk)
    except About.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of about
    if request.method == 'GET':
        serializer = AboutSerializer(about)
        return Response(serializer.data)
    # delete about
    elif request.method == 'DELETE':
        about.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
def get_delete_update_music(request, pk):
    try:
        music = Music.objects.get(pk = pk)
    except Music.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of music
    if request.method == 'GET':
        serializer = MusicSerializer(music)
        return Response(serializer.data)
    # delete music
    elif request.method == 'DELETE':
        music.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def get_delete_update_music(request, pk):
    try:
        music = Music.objects.get(pk = pk)
    except Music.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of music
    if request.method == 'GET':
        serializer = MusicSerializer(music)
        return Response(serializer.data)
    # delete music
    elif request.method == 'DELETE':
        music.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def get_post_about(request):
    #get all about
    if request.method == 'GET':
        about = About.objects.all()
        serializer = AboutSerializer(about, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'about': request.data.get('about')
        }
        serializer = AboutSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def get_post_music(request):
    #get all music
    if request.method == 'GET':
        music = Music.objects.all()
        serializer = MusicSerializer(music, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'music_player_url': request.data.get('music'),
            'bandcamp_url': request.data.get('music'),
            'song_title': request.data.get('music'),
            'last_update': request.data.get('music')
        }
        serializer = MusicSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)