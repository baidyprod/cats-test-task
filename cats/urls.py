from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MissionViewSet, SpyCatViewSet

router = DefaultRouter()
router.register(r"cats", SpyCatViewSet, basename="spycat")
router.register(r"missions", MissionViewSet, basename="mission")

urlpatterns = [
    path("", include(router.urls)),
]
