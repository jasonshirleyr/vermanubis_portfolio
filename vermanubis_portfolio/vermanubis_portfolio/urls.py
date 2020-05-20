from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('', include('frontend.urls')),
    path('', include('music.urls')),
    url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
]
