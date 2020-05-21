from django.conf.urls import url
from django.urls import path
from . import views

from rest_framework import routers
from .api import AboutViewSet, MusicViewSet

router = routers.DefaultRouter()

about_list = AboutViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

about_detail = AboutViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})


urlpatterns = [
    path('api/about/', about_list, name='about-list'),
    path('api/about/<int:pk>', about_detail, name='about-detail')
]

# register the router @ https://'appname'/api/music
# router.register(r'api/about', AboutViewSet, 'about')
# router.register(r'api/music', MusicViewSet, 'music')
# urlpatterns = router.urls

# urlpatterns = [
#     url(
#         r'^api/about/(?P<pk>[0-9]+)$',
#         views.get_delete_update_about,
#         name='get_delete_update_about'
#     ),
#     url(
#         r'^api/about/$',
#         views.get_post_about,
#         name='get_post_about'
#     ),
#     url(
#         r'^api/music/(?P<pk>[0-9]+)$',
#         views.get_delete_update_music,
#         name='get_delete_update_music'
#     ),
#     url(
#         r'^api/music/$',
#         views.get_post_music,
#         name='get_post_music'
#     )
# ]