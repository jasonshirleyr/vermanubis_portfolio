from rest_framework import routers
from .api import AboutViewSet, MusicViewSet

router = routers.DefaultRouter()

router.register('api/about', AboutViewSet, 'about')
router.register('api/music', MusicViewSet, 'music')
urlpatterns = router.urls
