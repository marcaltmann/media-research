from django.urls import path

from . import views

app_name = "archive"
urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("collections/", views.collection_index, name="collection_index"),
    path("collections/<int:collection_id>/", views.collection_detail,
         name="collection_detail"),
    path("interviews/", views.interview_index, name="interview_index"),
    path("interviews/<int:interview_id>/", views.interview_detail,
         name="interview_detail"),
    path("people/", views.person_index, name="person_index"),
    path("people/<int:person_id>/", views.person_detail, name="person_detail"),
    path("topics/", views.topic_index, name="topic_index"),
    path("topics/<int:topic_id>/", views.topic_detail, name="topic_detail"),
]
