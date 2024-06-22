from django.urls import path

from . import views

app_name = "entities"

urlpatterns = [
    path("", views.index, name="index"),
    path("people/", views.person_index, name="person_index"),
    path("people/<int:person_id>/", views.person_detail, name="person_detail"),
    path("locations/", views.LocationIndexView.as_view(), name="location_index"),
    path(
        "locations/<int:pk>/",
        views.LocationDetailView.as_view(),
        name="location_detail",
    ),
]
