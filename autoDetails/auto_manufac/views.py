from rest_framework import viewsets
from .permissions import ReadOnly, IsSuperAdminUser
from .models import CarDetail, Manufacturer
from .serializers import CarDetailSerializer, ManufacturerSerializer


class CarViewSet(viewsets.ModelViewSet):
    """
    Car view set to fetch, update, delete and create the car
    related information. Normal user can fetch and view the
    car information and superuser can perform the CRUD
    operation on car details.

    Accepted Method:
        GET, POST, PATCH, DELETE

    Endpoint:
        URL : /api/v1
        enpoints : cars
    """

    queryset = CarDetail.objects.all()
    serializer_class = CarDetailSerializer
    http_method_names = ["get", "post", "patch", "delete"]
    permission_classes = [IsSuperAdminUser | ReadOnly]


class ManufacturerView(viewsets.ModelViewSet):
    """
    Manufacturer view set to fetch, update, delete and create the
    car manufacturer related information. Normal user can fetch and
    view the car information and superuser can perform the CRUD
    operation on manufacturer of car details.

    Accepted Method:
        GET, POST, PATCH, DELETE

    Endpoint:
        URL : /api/v1
        enpoints : manufacturers
    """

    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    http_method_names = ["get", "post", "patch", "delete"]
    permission_classes = [IsSuperAdminUser | ReadOnly]
