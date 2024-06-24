from django.contrib import admin

from .models import Entity, Person, Location, Organisation, MiscellaneousEntity


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    list_display = ["name", "gnd_id"]


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["name", "latitude", "longitude"]


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ["name", "gnd_id"]


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ["name", "gnd_id"]


@admin.register(MiscellaneousEntity)
class MiscellaneousEntityAdmin(admin.ModelAdmin):
    list_display = ["name", "gnd_id"]
