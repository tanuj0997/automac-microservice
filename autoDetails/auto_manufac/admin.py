from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site
from .models import CarDetail, Manufacturer


class ManufacturerAdmin(admin.ModelAdmin):
    model = Manufacturer
    list_display = [
        "name",
        "country",
    ]
    search_fields = ("name",)
    ordering = ("country",)


class CarDetailAdmin(admin.ModelAdmin):
    model = CarDetail
    list_display = ["name", "color", "door"]
    search_fields = ("name",)


admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(CarDetail, CarDetailAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)
