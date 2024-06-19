from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("terms/", views.terms, name="terms"),
    path("privacy/", views.privacy, name="privacy"),
    path("accessibility/", views.accessibility, name="accessibility"),
]
