from rest_framework import serializers
from automobile.models import Tesla


class TeslaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tesla
        fields = "__all__"
