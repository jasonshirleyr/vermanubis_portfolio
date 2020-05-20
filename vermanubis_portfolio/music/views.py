from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import About
from .serializers import AboutSerializer

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_about(request, pk):
    try:
        about = About.objects.get(pk=pk)
    except About.DoesNotExist:
        return Response(satus=status.HTTP_404_NOT_FOUND)

    # get details of about
    if request.method == 'GET':
        return Response({})
    # delete about
    elif request.method == 'DELETE':
        return Response({})
    elif request.method == 'PUT':
        return Response({})

@api_view(['GET', 'POST'])
def get_post_about(request):
    
    #get about
    if request.method == 'GET':
        return Response({})
    elif request.method == 'POST':
        return Response ({})