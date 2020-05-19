from rest_framework import routers
from .api import AboutViewSet

router = routers.DefaultRouter()

# register the router @ https://'appname'/api/music
router.register('api/about', AboutViewSet, 'about')

urlpatterns = router.urls