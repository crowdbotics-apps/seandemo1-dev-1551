from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import TeslaViewSet

router = DefaultRouter()
router.register("tesla", TeslaViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
