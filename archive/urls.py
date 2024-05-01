from django.urls import path

from . import views

app_name = "archive"
urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("search/", views.search, name="search"),
    path("collections/", views.CollectionIndexView.as_view(),
         name="collection_index"),
    path("collections/<int:collection_id>/", views.collection_detail,
         name="collection_detail"),
    path("resources/", views.ResourceIndexView.as_view(),
         name="resource_index"),
    path("resources/<int:resource_id>/", views.resource_detail,
         name="resource_detail"),
    path("people/", views.person_index, name="person_index"),
    path("people/<int:person_id>/", views.person_detail, name="person_detail"),
    path("topics/", views.topic_index, name="topic_index"),
    path("topics/<int:topic_id>/", views.topic_detail, name="topic_detail"),
    path("locations/", views.LocationIndexView.as_view(),
         name="location_index"),
    path("locations/<int:pk>/", views.LocationDetailView.as_view(),
         name="location_detail"),
    path("profile/", views.profile, name="profile"),
    path("terms/", views.terms, name="terms"),
    path("privacy/", views.privacy, name="privacy"),
    path("accessibility/", views.accessibility, name="accessibility"),
]
