from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api import views as api_views

router = routers.DefaultRouter()
router.register(r"resources", api_views.ResourceViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("__debug__/", include("debug_toolbar.urls")),
]

urlpatterns += i18n_patterns(
    path("", include("pages.urls")),
    path("", include("archive.urls")),
    path("entities/", include("entities.urls")),
    path("materials/", include("materials.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
    path("admin/", admin.site.urls),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
