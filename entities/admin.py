from django.contrib import admin

from .models import Entity, Location, Person


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    list_display = ["name", "type", "gnd_id"]


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["name", "latitude", "longitude"]


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ["last_name", "first_name"]
    list_display = ["last_name", "first_name", "gender", "date_of_birth"]
