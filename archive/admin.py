from django.contrib import admin

from archive.models import (
    Resource,
    Collection,
    Transcript,
    Person,
    ResourceInvolvement,
    Topic,
    TopicReference,
    MetadataKey,
    CharFieldMetadata,
    Location,
    LocationReference,
)


class TopicReferenceInline(admin.TabularInline):
    model = TopicReference
    extra = 1


class LocationReferenceInline(admin.TabularInline):
    model = LocationReference
    extra = 1


class ResourceInvolvementInline(admin.TabularInline):
    model = ResourceInvolvement
    extra = 1


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title", "media_type", "duration", "public", "is_video"]
    list_filter = ["pub_date", "media_type", "public"]
    fieldsets = [
        (None, {"fields": ["title", "pub_date", "duration", "public"]}),
        ("Media information", {"fields": ["media_type", "media_url", "poster"]}),
    ]
    inlines = [
        TopicReferenceInline,
        LocationReferenceInline,
        ResourceInvolvementInline,
    ]


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    search_fields = ["name", "description"]
    fields = ["name", "description", "resources"]
    list_display = ["name", "resource_count"]
    filter_horizontal = ["resources"]


@admin.register(Transcript)
class TranscriptAdmin(admin.ModelAdmin):
    search_fields = ["vtt"]
    list_display = ["resource", "language"]


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ["last_name", "first_name"]
    list_display = ["last_name", "first_name", "gender", "date_of_birth"]


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    search_fields = ["name", "gnd_id"]
    list_display = ["name", "gnd_id"]


@admin.register(MetadataKey)
class MetadataKeyAdmin(admin.ModelAdmin):
    search_fields = ["label"]
    list_display = ["label"]


@admin.register(CharFieldMetadata)
class CharFieldMetadataAdmin(admin.ModelAdmin):
    list_display = ["resource", "key", "value"]


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["name", "latitude", "longitude"]
