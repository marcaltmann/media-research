from django.contrib import admin
from django.db.models import JSONField
from django_json_widget.widgets import JSONEditorWidget

from .models import Entity


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    list_display = ["name", "type"]
    list_filter = ["type"]
    search_fields = ["name"]
    formfield_overrides = {
        JSONField: {"widget": JSONEditorWidget},
    }
