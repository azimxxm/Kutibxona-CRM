from rest_framework import routers
from .api import *

router = routers.DefaultRouter()
router.register('lavozim', LavozimViewSet, 'lavozim'),




urlpatterns = router.urls