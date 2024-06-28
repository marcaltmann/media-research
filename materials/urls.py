from django.urls import path

from . import views

app_name = "materials"

urlpatterns = [
    path(
        "<int:image_material_id>/",
        views.image_material_detail,
        name="image_material_detail",
    ),
]
