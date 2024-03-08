from django.urls import path

from . import views

app_name = "archive"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:archive_id>/", views.detail, name="detail"),
    path("<int:archive_id>/interviews/<int:interview_id>/",
         views.interview, name="interview"),
]
