from django.urls import path
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'spaceships', SpaceShipViewSet)
router.register(r'crew', CrewViewSet)


urlpatterns = router.urls