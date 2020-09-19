from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework import status
from rest_framework.authtoken.models import Token
from .permissions import IsSuperAdminUser
from .serializers import (
    UserRegistrationSerializer,
    AuthTokenSerializer,
    UserLogoutSerializer,
)

from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationViewset(viewsets.ModelViewSet):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()
    http_method_names = ["post", "patch", "delete"]
    permission_classes = [IsSuperAdminUser]
    authentication_classes = [BasicAuthentication]

    def create(self, request):
        """
        URL : /api/v1/users/
        Endpoints : /users/
        Accepted Method : POST
        Accepted Param in body:
         {
            "first_name": "",
            "last_name": "",
            "email": "",
            "user_password": ""
        }
        Accepted success response:
        {
            "token": "ce80f75182ae74bf851d3d7d32941152ed43521e"
        }
        """
        serializer = self.serializer_class(data=request.data)
        # check serializer is valid or not.
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response(
                {
                    "token": user.auth_token.key,
                },
                status.HTTP_201_CREATED,
            )


class ObtainUserAuthToken(APIView):
    """
    IT's user login view. accepted method post. it's return always new token.
        URL : /api/v1/login/
        Endpoints : /login/
        Accepted Method : POST
        Accepted Param in body:
        {
            "email": "",
            "password": ""
        }
        Accepted success response:
        {
            "token": "",
            "first_name" : ""
        }
    """

    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data["user"]
            token, created = Token.objects.get_or_create(user=user)

            return Response(
                {
                    "token": token.key,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "is_superuser": user.is_superuser,
                },
                status.HTTP_200_OK,
            )


class UserLogout(APIView):
    """
    IT's user logout view. accepted method post.
        URL : /api/v1/logout/
        Endpoints : /logout/
        Accepted Method : POST
        Accepted Param in body:
        {
            "token": ""
        }
        Accepted success response:
        {
            "status": 200,
            "message": "Successfully logout."
        }
    """

    serializer_class = UserLogoutSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        token = serializer.validated_data["token"]
        token.delete()

        return Response(
            {"status": status.HTTP_200_OK, "message": "Successfully logout."}
        )
