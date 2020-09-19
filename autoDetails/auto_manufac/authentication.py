import requests
from threading import local
from django.conf import settings
from django.contrib.auth.backends import ModelBackend

from django.contrib.auth.models import User
from django.contrib.auth.models import Group

_stash = local()


class AuthenticationBackend(ModelBackend):
    """
    Authenticate the user through other service and create the session in the currect service.
    """

    def authenticate(self, request, **credentials):
        ret = None
        ret = self._authenticate_by_email(**credentials)
        if ret:
            return ret
        return ret

    def _authenticate_by_email(self, **credentials):
        email = credentials.get("email", credentials.get("username"))
        if email:
            url = settings.AUTHENTICATION_SERVICE_SECOND
            data = {"email": email, "password": credentials.get("password")}
            res = requests.post(url, data=data)
            if res.ok and res.status_code == 200:
                user, created = User.objects.get_or_create(
                    email=email,
                    username=email,
                    is_staff=True,
                    is_active=True,
                    is_superuser=res.json()["is_superuser"],
                    first_name=res.json()["first_name"],
                    last_name=res.json()["last_name"],
                )
                if created and not res.json()["is_superuser"]:
                    group = Group.objects.first()
                    user.groups.add(group)
                    user.save()
                return user
                self._stash_user(user)
        return None

    @classmethod
    def _stash_user(cls, user):
        global _stash
        ret = getattr(_stash, "user", None)
        _stash.user = user
        return ret

    @classmethod
    def unstash_authenticated_user(cls):
        return cls._stash_user(None)
