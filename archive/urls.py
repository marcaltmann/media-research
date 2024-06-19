from django.urls import path

from . import views

app_name = "archive"
urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("search/", views.search, name="search"),
    path("collections/", views.CollectionIndexView.as_view(), name="collection_index"),
    path(
        "collections/<int:collection_id>/",
        views.collection_detail,
        name="collection_detail",
    ),
    path("resources/", views.ResourceIndexView.as_view(), name="resource_index"),
    path("resources/<int:resource_id>/", views.resource_detail, name="resource_detail"),
    path("profile/", views.profile, name="profile"),
    path("terms/", views.terms, name="terms"),
    path("privacy/", views.privacy, name="privacy"),
    path("accessibility/", views.accessibility, name="accessibility"),
]
