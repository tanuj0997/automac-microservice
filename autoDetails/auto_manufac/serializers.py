from rest_framework import serializers
from .models import CarDetail, Manufacturer


class CarDetailSerializer(serializers.ModelSerializer):
    """
    Car detail serializer to validate the data before save the car details.
    """

    class Meta:
        model = CarDetail
        fields = "__all__"


class ManufacturerSerializer(serializers.ModelSerializer):
    """
    Manufacturer serializer to validate the car manufacturer data before the save.
    """

    class Meta:
        model = Manufacturer
        fields = "__all__"
