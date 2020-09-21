from django.core.management.base import BaseCommand

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group, Permission
from auto_manufac.models import CarDetail, Manufacturer


class Command(BaseCommand):
    def handle(self, *args, **options):
        group, _ = Group.objects.get_or_create(name="viewer")

        car_ct = ContentType.objects.get_for_model(CarDetail)
        manufacturer_ct = ContentType.objects.get_for_model(Manufacturer)

        view_cardetail = Permission.objects.get(
            content_type=car_ct, codename="view_cardetail"
        )
        view_manufac = Permission.objects.get(
            content_type=manufacturer_ct, codename="view_manufacturer"
        )

        group.permissions.add(view_cardetail)
        group.permissions.add(view_manufac)

        group.save()
