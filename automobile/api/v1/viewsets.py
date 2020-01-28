from rest_framework import authentication
from automobile.models import Tesla
from .serializers import TeslaSerializer
from rest_framework import viewsets


class TeslaViewSet(viewsets.ModelViewSet):
    serializer_class = TeslaSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Tesla.objects.all()
