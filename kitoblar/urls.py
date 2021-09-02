from django.urls import path
from . import views
from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

urlpatterns = [
    path('', views.home, name='home'),
]

router.register('api/lavozim', LavozimViewSet, 'lavozim'),
router.register('api/xodimlar', XodimlarViewSet, 'xodimlar'),
router.register('api/janir', JanrViewSet, 'janir'),
router.register('api/nashriyot', NashriyotViewSet, 'nashriyot'),
router.register('api/kitob_tillari', Kitob_tillariViewSet, 'kitob_tillari'),
router.register('api/student', StudentViewSet, 'student'),
router.register('api/kitoblar', KitoblarViewSet, 'kitoblar'),
router.register('api/berilgan_kitoblar', Berilgan_kitoblarViewSet, 'berilgan_kitoblar'),


urlpatterns += router.urls

