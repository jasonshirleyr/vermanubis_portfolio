from rest_framework import routers
from .api import AboutViewSet, MusicViewSet

router = routers.DefaultRouter()

router.register(r'api/about', AboutViewSet, 'about')
router.register(r'api/music', MusicViewSet, 'music')
urlpatterns = router.urls
