from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("accessibility/", views.accessibility, name="accessibility"),
    path("contact/", views.contact, name="contact"),
    path("legal_notice/", views.legal_notice, name="legal_notice"),
    path("privacy/", views.privacy, name="privacy"),
]
