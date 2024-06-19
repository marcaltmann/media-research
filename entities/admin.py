from django.contrib import admin

from .models import Location, Person, Topic


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["name", "latitude", "longitude"]


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ["last_name", "first_name"]
    list_display = ["last_name", "first_name", "gender", "date_of_birth"]


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    search_fields = ["name", "gnd_id"]
    list_display = ["name", "gnd_id"]
