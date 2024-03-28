from django.contrib import admin

from archive.models import (Interview, Collection, Transcript,
                            Person, InterviewInvolvement, Topic,
                            TopicReference, MetadataKey, CharFieldMetadata,
                            Location, LocationReference)


class TopicReferenceInline(admin.TabularInline):
    model = TopicReference
    extra = 1


class LocationReferenceInline(admin.TabularInline):
    model = LocationReference
    extra = 1


class InterviewInvolvementInline(admin.TabularInline):
    model = InterviewInvolvement
    extra = 1


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
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
        InterviewInvolvementInline,
    ]


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    search_fields = ["name", "description"]
    fields = ["name", "description", "interviews"]
    list_display = ["name", "interview_count"]
    filter_horizontal = ["interviews"]


@admin.register(Transcript)
class TranscriptAdmin(admin.ModelAdmin):
    search_fields = ["vtt"]
    list_display = ["interview", "language"]


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
    list_display = ["interview", "key", "value"]


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["name", "latitude", "longitude"]
