from django.urls import path

from . import views

app_name = "entities"

urlpatterns = [
    path("", views.entity_index, name="entity_index"),
    path("<int:entity_id>/", views.entity_detail, name="entity_detail"),
]
