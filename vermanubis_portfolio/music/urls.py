from rest_framework import routers
from .api import MusicViewSet

router = routers.DefaultRouter()

# register the router @ https://'appname'/api/music
router.register('api/music', MusicViewSet, 'music')

urlpatterns = router.urls